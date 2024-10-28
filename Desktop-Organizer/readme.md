````markdown
# Desktop Organizer

## 简介

**Desktop Organizer** 是一个用于整理 Windows 桌面文件的 Python 脚本。它根据文件类型将桌面上的文件移动到预定义的分类文件夹中，并支持撤回整理操作。此外，脚本会在每次运行后自动尝试将桌面图标按名称排序，以保持桌面整洁有序。如果排序失败，脚本会自动重新启动 `explorer.exe` 以刷新桌面图标排列。

## 功能

- **分类整理**：根据文件扩展名将桌面文件移动到相应的分类文件夹中。
- **撤回操作**：根据记录的操作日志，将文件恢复到原始位置。
- **自动排列图标**：每次整理后，尝试将桌面图标按名称排序，确保非文件夹快捷方式位于左侧，文件夹位于右侧。
- **异常处理**：在排列图标失败时，自动重新启动 `explorer.exe` 以刷新桌面。

## 分类规则

脚本根据以下分类规则整理桌面文件：

- **Applications**: `.lnk`, `.exe`, `.msi`
- **Documents**: `.docx`, `.xlsx`, `.pptx`, `.pdf`, `.txt`, `.md`
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
- **Videos**: `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`
- **Music**: `.mp3`, `.wav`, `.aac`, `.flac`
- **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- **Scripts**: `.py`, `.bat`, `.sh`, `.ps1`
- **Others**: 其他未分类的文件

## 安装

### 前提条件

- **Python 3.x**：确保你的系统中已安装 Python 3.x。你可以从 [Python 官方网站](https://www.python.org/downloads/) 下载并安装。
- **pip**：Python 的包管理工具，通常与 Python 一起安装。

### 克隆仓库

```bash
git clone https://github.com/ChuheZhang/python-tools.git
cd Desktop-Organizer
```
````

### 安装依赖

本脚本依赖于 `pywin32` 库，用于与 Windows Shell 进行交互。使用以下命令安装：

```bash
pip install pywin32
```

## 使用说明

将 `OrganizeDesktop.py` 脚本放置在任意目录（推荐桌面或你的项目目录）中，并按照以下步骤运行。

### 运行脚本

打开命令提示符或 PowerShell，导航到脚本所在目录，并使用以下命令运行：

#### 整理桌面文件

```bash
python OrganizeDesktop.py organize
```

**示例输出**：

```
已创建 'Folders' 文件夹。
已创建 'Applications' 文件夹。
已创建 'Documents' 文件夹。
已创建 'Images' 文件夹。
已创建 'Videos' 文件夹。
已创建 'Music' 文件夹。
已创建 'Archives' 文件夹。
已创建 'Scripts' 文件夹。
Moved: example.exe -> Applications/
Moved: report.docx -> Documents/
Moved folder: Projects -> Folders/
桌面整理完成。
桌面图标已按名称排序。
```

#### 撤回整理操作

```bash
python OrganizeDesktop.py undo
```

**示例输出**：

```
Moved back: example.exe -> Applications/
Moved back: report.docx -> Documents/
Moved back: Projects -> Folders/
撤回操作完成，桌面已恢复原状。
桌面图标已按名称排序。
```

### 参数说明

- `organize`：执行桌面文件的分类整理，并排列图标。
- `undo`：撤回最近一次的整理操作，将文件恢复到原始位置，并重新排列图标。

## 工作原理

1. **分类整理** (`organize_desktop` 函数)：

   - **创建分类文件夹**：根据 `CATEGORIES` 字典创建相应的文件夹（如 `Applications`、`Documents` 等）。
   - **移动文件**：
     - **非文件夹快捷方式和文件**：将桌面上的快捷方式（如 `.lnk`、`.exe`、`.msi` 文件）和其他文件根据扩展名移动到对应的分类文件夹中。
     - **文件夹**：将桌面上的其他文件夹移动到一个名为 `Folders` 的文件夹中。
   - **记录操作**：所有移动操作记录保存在 `desktop_backup.json` 文件中，以便后续撤回。
   - **排列桌面图标**：调用 `arrange_icons_by_name` 函数，尝试将桌面图标按名称排序。如果排序失败，自动重新启动 `explorer.exe` 以刷新桌面。

2. **撤回整理** (`undo_organize` 函数)：

   - **读取备份文件**：从 `desktop_backup.json` 文件中读取所有移动操作记录。
   - **移动回原位**：将文件和文件夹从分类文件夹移动回原始位置。
   - **删除备份文件**：删除 `desktop_backup.json` 文件，完成撤回操作。
   - **排列桌面图标**：再次调用 `arrange_icons_by_name` 函数，尝试将桌面图标按名称排序。如果排序失败，自动重新启动 `explorer.exe` 以刷新桌面。

3. **排列桌面图标** (`arrange_icons_by_name` 函数)：
   - **使用 COM 接口尝试排列图标**：通过 `pywin32` 库与 Windows Shell 交互，调用 `view.Sort` 方法将桌面图标按名称排序。
   - **重新启动 Explorer 以刷新图标**：如果 COM 方法失败，脚本会自动重新启动 `explorer.exe`，强制 Windows 刷新桌面图标排列。

## 权限

- **管理员权限**：为确保脚本能够读取和写入桌面上的所有文件和文件夹，建议以管理员身份运行命令提示符或 PowerShell。
  - 右键点击 **命令提示符** 或 **PowerShell**，选择 **以管理员身份运行**。

## 注意事项

- **备份数据**：虽然脚本会创建 `desktop_backup.json` 文件记录所有移动操作，以支持撤回，但强烈建议在运行脚本前备份重要数据。
- **脚本限制**：
  - Windows 对桌面图标排列的编程控制有限，脚本通过 `pywin32` 和重新启动 `explorer.exe` 尝试设置图标排序，但效果可能因系统配置和版本而异。
  - 图标排序功能依赖于 Windows Shell，无法保证完全按照非文件夹快捷方式在左、文件夹在右的顺序排列。
- **文件冲突**：如果目标文件夹中已经存在同名文件，`shutil.move` 将覆盖目标文件。建议在使用前确认桌面文件的唯一性，或根据需要修改脚本以处理文件冲突（如重命名文件或跳过已存在的文件）。

## 常见问题

### 1. 排列桌面图标时发生错误：`(-2147352562, '无效的参数数目。', None, None)`

**原因**：

- 原先的 `SortColumns.Add` 方法调用参数数量不正确，导致 `Invalid number of parameters` 错误。

**解决方案**：

- 在修正后的脚本中，移除了对 `SortColumns.Clear()` 和 `SortColumns.Add()` 的调用，仅调用 `view.Sort(0, 1)`，确保传递正确数量和类型的参数。

### 2. 权限错误

**错误信息**：

```
PermissionError: [WinError 32] 另一个程序正在使用此文件，进程无法访问。: 'C:\\Users\\Fatin\\Desktop\\Folders' -> 'C:\\Users\\Fatin\\Desktop\\Folders\\Folders'
```

**解决方案**：

- **确保脚本排除了 `Folders` 和 `Others` 文件夹**：在整理文件夹时，脚本已排除这些文件夹，避免将其移动到自身的子文件夹中。
- **关闭占用文件的程序**：确保桌面上的文件和文件夹没有被其他程序占用。关闭所有可能使用这些文件或文件夹的程序。
- **以管理员身份运行**：右键点击 **命令提示符** 或 **PowerShell**，选择 **以管理员身份运行**，然后重新运行脚本。

### 3. 无法导入 `win32com.client` 模块

**解决方案**：

- 确保已正确安装 `pywin32` 库：

  ```bash
  pip install pywin32
  ```

- 确保使用的 Python 环境与安装库的环境一致。如果使用的是虚拟环境，确保已激活虚拟环境后再安装和运行脚本。

### 4. 脚本未能成功排列图标

**解决方案**：

- **确保 `arrange_icons_by_name` 函数调用正确**：在修正后的脚本中，`view.Sort(0, 1)` 已被正确调用。
- **手动设置排序方式**：如果脚本仍然无法成功排列图标，可以手动设置排序方式：
  1. **右键点击桌面空白处**。
  2. 选择 **“排序方式”** -> **“名称”**。
- **检查 `pywin32` 版本**：确保你使用的是最新版本的 `pywin32`，以避免因版本不兼容导致的问题。

## 贡献

欢迎贡献代码、提出问题或建议！请提交 [Issue](https://github.com/ChuheZhang/python-tools/issues) 或 [Pull Request](https://github.com/ChuheZhang/python-tools/pulls)。

## 许可证

本项目采用 [MIT 许可证](LICENSE)。

## 致谢

感谢所有为本项目提供支持和建议的朋友们！

```

```
