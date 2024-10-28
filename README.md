
# Python Tools

## 简介

**Python Tools** 是一个多功能的 Python 脚本集合，旨在通过自动化和简化日常任务来提高工作效率。无论你是开发者、数据分析师，还是普通用户，这个仓库都提供了多种实用工具，帮助你更高效地完成各种任务。

## 目录

- [功能概述](#功能概述)
- [安装](#安装)
- [使用说明](#使用说明)
  - [桌面整理工具](#桌面整理工具)
  - [其他工具](#其他工具)
- [贡献](#贡献)
- [许可证](#许可证)
- [致谢](#致谢)

## 功能概述

当前仓库包含以下工具：

1. **桌面整理工具** (`OrganizeDesktop.py`)
   - **描述**：自动整理 Windows 桌面文件，根据文件类型将文件移动到预定义的分类文件夹中，并支持撤回操作。同时，尝试将桌面图标按名称排序，保持桌面整洁有序。
   
2. **文件批量重命名工具** (`BatchRename.py`)
   - **描述**：批量重命名指定文件夹中的文件，支持自定义命名规则，如添加前缀、后缀、编号等。
   
3. **图片格式转换工具** (`ImageConverter.py`)
   - **描述**：将指定文件夹中的图片批量转换为另一种格式（如从 PNG 转换为 JPEG）。
   
4. **PDF 合并工具** (`MergePDFs.py`)
   - **描述**：合并多个 PDF 文件为一个单一的 PDF 文件，支持自定义合并顺序。
   
5. **网络爬虫工具** (`WebScraper.py`)
   - **描述**：从指定的网站抓取数据，支持自定义抓取规则和数据存储格式。

## 安装

### 前提条件

- **Python 3.x**：确保你的系统中已安装 Python 3.x。你可以从 [Python 官方网站](https://www.python.org/downloads/) 下载并安装。
- **pip**：Python 的包管理工具，通常与 Python 一起安装。

### 克隆仓库

```bash
git clone https://github.com/ChuheZhang/python-tools.git
cd python-tools
```

### 安装依赖

根据你需要使用的工具，安装相应的依赖包。以下是一些常用工具的依赖安装示例：

#### 桌面整理工具

```bash
pip install pywin32
```

#### 文件批量重命名工具

```bash
pip install argparse
```

#### 图片格式转换工具

```bash
pip install Pillow
```

#### PDF 合并工具

```bash
pip install PyPDF2
```

#### 网络爬虫工具

```bash
pip install requests beautifulsoup4
```

## 使用说明

### 桌面整理工具

**脚本名称**：`OrganizeDesktop.py`

**描述**：自动整理 Windows 桌面文件，根据文件类型将文件移动到预定义的分类文件夹中，并支持撤回操作。同时，尝试将桌面图标按名称排序，保持桌面整洁有序。

#### 运行整理命令

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

### 文件批量重命名工具

**脚本名称**：`BatchRename.py`

**描述**：批量重命名指定文件夹中的文件，支持自定义命名规则，如添加前缀、后缀、编号等。

#### 使用示例

```bash
python BatchRename.py --folder "C:\Users\Fatin\Documents\Reports" --prefix "Report_" --start 1
```

**参数说明**：

- `--folder`：指定要重命名的文件夹路径。
- `--prefix`：为文件添加前缀。
- `--start`：编号开始值。

### 图片格式转换工具

**脚本名称**：`ImageConverter.py`

**描述**：将指定文件夹中的图片批量转换为另一种格式（如从 PNG 转换为 JPEG）。

#### 使用示例

```bash
python ImageConverter.py --input "C:\Users\Fatin\Pictures" --output "C:\Users\Fatin\ConvertedImages" --format "JPEG"
```

**参数说明**：

- `--input`：指定输入文件夹路径。
- `--output`：指定输出文件夹路径。
- `--format`：目标图片格式（如 JPEG, PNG）。

### PDF 合并工具

**脚本名称**：`MergePDFs.py`

**描述**：合并多个 PDF 文件为一个单一的 PDF 文件，支持自定义合并顺序。

#### 使用示例

```bash
python MergePDFs.py --input "C:\Users\Fatin\Documents\PDFs" --output "C:\Users\Fatin\Documents\Merged.pdf"
```

**参数说明**：

- `--input`：指定包含 PDF 文件的文件夹路径。
- `--output`：指定合并后 PDF 文件的保存路径。

### 网络爬虫工具

**脚本名称**：`WebScraper.py`

**描述**：从指定的网站抓取数据，支持自定义抓取规则和数据存储格式。

#### 使用示例

```bash
python WebScraper.py --url "https://example.com" --output "C:\Users\Fatin\Documents\data.json"
```

**参数说明**：

- `--url`：指定要抓取数据的网站 URL。
- `--output`：指定抓取数据的保存路径和格式（如 JSON, CSV）。

## 贡献

欢迎贡献代码、提出问题或建议！请按照以下步骤进行：

1. Fork 本仓库。
2. 创建你的特性分支：`git checkout -b feature/YourFeature`
3. 提交你的更改：`git commit -m 'Add some feature'`
4. 推送到分支：`git push origin feature/YourFeature`
5. 打开一个 Pull Request。

请确保你的代码遵循 PEP 8 规范，并包含必要的文档和注释。

## 许可证

本项目采用 [MIT 许可证](LICENSE) 许可。

## 致谢

- 感谢所有为本项目提供支持和建议的朋友们！
- 特别感谢 [PyWin32](https://github.com/mhammond/pywin32)、[Pillow](https://python-pillow.org/)、[PyPDF2](https://github.com/mstamy2/PyPDF2) 等开源项目，为本工具提供了强大的功能支持。
