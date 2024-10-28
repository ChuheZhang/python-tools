import os
import shutil
import json
import argparse
from pathlib import Path
import win32com.client
import subprocess
import time

# 定义桌面路径
DESKTOP_PATH = Path.home() / "Desktop"
BACKUP_FILE = DESKTOP_PATH / "desktop_backup.json"

# 定义分类规则
CATEGORIES = {
    "Applications": [".lnk", ".exe", ".msi"],
    "Documents": [".docx", ".xlsx", ".pptx", ".pdf", ".txt", ".md"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".bat", ".sh", ".ps1"],
    "Others": []  # 默认分类
}

def load_backup():
    if BACKUP_FILE.exists():
        with open(BACKUP_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_backup(backup_data):
    with open(BACKUP_FILE, 'w', encoding='utf-8') as f:
        json.dump(backup_data, f, ensure_ascii=False, indent=4)

def restart_explorer():
    try:
        print("正在重新启动 Explorer 以刷新桌面图标...")
        subprocess.call(['taskkill', '/F', '/IM', 'explorer.exe'])
        time.sleep(1)
        subprocess.Popen(['explorer.exe'])
        print("Explorer 已重新启动。")
    except Exception as e:
        print(f"重新启动 Explorer 时发生错误: {e}")

def arrange_icons_by_name():
    try:
        # 使用 COM 接口尝试排列图标
        shell = win32com.client.Dispatch("Shell.Application")
        desktop = shell.Namespace(0)  # 0代表桌面
        folder = desktop.Self.GetFolder()
        view = folder.View

        # 尝试按名称排序
        # 参数：column index 0 (名称), ascending=True
        view.Sort(0, True)  # 0: Name, True: Ascending
        print("桌面图标已按名称排序。")
    except Exception as e:
        print(f"排列桌面图标时发生错误: {e}")
        # 如果 COM 方法失败，尝试重新启动 Explorer
        restart_explorer()

def organize_desktop():
    backup_data = []

    # 确保 'Folders' 文件夹存在，并排除它不被移动
    folders_folder = DESKTOP_PATH / "Folders"
    if not folders_folder.exists():
        try:
            folders_folder.mkdir()
            print("已创建 'Folders' 文件夹。")
        except Exception as e:
            print(f"创建 'Folders' 文件夹时发生错误: {e}")
            return

    # 创建其他分类文件夹
    for category in CATEGORIES.keys():
        folder = DESKTOP_PATH / category
        if not folder.exists():
            try:
                folder.mkdir()
                print(f"已创建 '{category}' 文件夹。")
            except Exception as e:
                print(f"创建 '{category}' 文件夹时发生错误: {e}")

    # 优先整理非文件夹快捷方式和文件
    for item in DESKTOP_PATH.iterdir():
        if item.is_file() and item.name != BACKUP_FILE.name:
            destination = None
            for category, extensions in CATEGORIES.items():
                if item.suffix.lower() in extensions:
                    destination = DESKTOP_PATH / category / item.name
                    break
            if not destination:
                destination = DESKTOP_PATH / "Others" / item.name

            # 如果文件已经在目标文件夹中，跳过
            if item.parent == destination.parent:
                continue

            try:
                # 移动文件并记录操作
                shutil.move(str(item), str(destination))
                backup_data.append({
                    "original_path": str(item),
                    "new_path": str(destination)
                })
                print(f"Moved: {item.name} -> {destination.parent.name}/")
            except Exception as e:
                print(f"移动文件 '{item.name}' 时发生错误: {e}")

    # 然后整理文件夹，排除 'Folders' 和 'Others' 文件夹本身
    for item in DESKTOP_PATH.iterdir():
        if item.is_dir() and item.name not in CATEGORIES.keys() and item.name not in ["Others", "Folders"]:
            destination = DESKTOP_PATH / "Folders" / item.name
            if not (DESKTOP_PATH / "Folders").exists():
                try:
                    (DESKTOP_PATH / "Folders").mkdir()
                    print("已创建 'Folders' 文件夹。")
                except Exception as e:
                    print(f"创建 'Folders' 文件夹时发生错误: {e}")
                    continue  # 跳过当前文件夹

            if item.parent == destination.parent:
                continue

            try:
                shutil.move(str(item), str(destination))
                backup_data.append({
                    "original_path": str(item),
                    "new_path": str(destination)
                })
                print(f"Moved folder: {item.name} -> Folders/")
            except Exception as e:
                print(f"移动文件夹 '{item.name}' 时发生错误: {e}")

    # 无论是否有文件被移动，都尝试排列桌面图标
    if backup_data:
        save_backup(backup_data)
        print("桌面整理完成。")
    else:
        print("没有需要整理的文件。")

    arrange_icons_by_name()

def undo_organize():
    if not BACKUP_FILE.exists():
        print("找不到备份文件，无法撤回。")
        return

    backup_data = load_backup()
    if not backup_data:
        print("备份文件为空，无法撤回。")
        return

    for entry in backup_data:
        original = Path(entry["original_path"])
        new = Path(entry["new_path"])

        if new.exists():
            try:
                # 确保原始文件夹存在
                original.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(new), str(original))
                print(f"Moved back: {new.name} -> {original.parent.name}/")
            except Exception as e:
                print(f"移动回文件 '{new.name}' 时发生错误: {e}")
        else:
            print(f"文件不存在，无法移动回: {new}")

    # 删除备份文件
    try:
        BACKUP_FILE.unlink()
        print("撤回操作完成，桌面已恢复原状。")
    except Exception as e:
        print(f"删除备份文件时发生错误: {e}")

    arrange_icons_by_name()

def main():
    parser = argparse.ArgumentParser(description="整理桌面文件或撤回整理操作。")
    subparsers = parser.add_subparsers(dest='command', help='子命令')

    # 子命令：organize
    parser_organize = subparsers.add_parser('organize', help='整理桌面文件')

    # 子命令：undo
    parser_undo = subparsers.add_parser('undo', help='撤回桌面整理操作')

    args = parser.parse_args()

    if args.command == 'organize':
        organize_desktop()
    elif args.command == 'undo':
        undo_organize()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
