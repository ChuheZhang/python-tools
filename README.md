# Python Tools

## Description

This repository predominantly consists of functional Python scripts developed for personal use. These tools are designed to streamline daily tasks, resolve minor inconveniences, and address specific office needs for my mother.

## Features

- **Desktop Organizer**: Automatically organizes desktop files into categorized folders and sorts desktop icons by name.
- **Batch Rename**: Bulk renames files in a specified directory based on customizable naming rules.
- **Image Converter**: Converts images from one format to another in bulk.
- **PDF Merger**: Combines multiple PDF files into a single document.
- **Web Scraper**: Extracts data from websites based on defined scraping rules.

## Installation

### Prerequisites

- **Python 3.x**: Ensure Python 3.x is installed on your system. Download it from the [official website](https://www.python.org/downloads/).
- **pip**: Python's package installer, typically included with Python installations.

### Clone the Repository

```bash
git clone https://github.com/ChuheZhang/python-tools.git
cd python-tools
```

### Install Dependencies

Install the required Python packages for each tool as needed. For example:

#### Desktop Organizer

```bash
pip install pywin32
```

#### Batch Rename

```bash
pip install argparse
```

#### Image Converter

```bash
pip install Pillow
```

#### PDF Merger

```bash
pip install PyPDF2
```

#### Web Scraper

```bash
pip install requests beautifulsoup4
```

## Usage

### Desktop Organizer

**Script Name**: `OrganizeDesktop.py`

**Description**: Automatically organizes Windows desktop files into predefined categories and attempts to sort desktop icons by name. If sorting fails, it restarts `explorer.exe` to refresh the desktop.

**Run Organize Command**

```bash
python OrganizeDesktop.py organize
```

**Run Undo Command**

```bash
python OrganizeDesktop.py undo
```

### Batch Rename

**Script Name**: `BatchRename.py`

**Description**: Bulk renames files in a specified directory based on customizable naming rules.

**Example Usage**

```bash
python BatchRename.py --folder "C:\Users\Fatin\Documents\Reports" --prefix "Report_" --start 1
```

### Image Converter

**Script Name**: `ImageConverter.py`

**Description**: Converts images from one format to another in bulk.

**Example Usage**

```bash
python ImageConverter.py --input "C:\Users\Fatin\Pictures" --output "C:\Users\Fatin\ConvertedImages" --format "JPEG"
```

### PDF Merger

**Script Name**: `MergePDFs.py`

**Description**: Combines multiple PDF files into a single document.

**Example Usage**

```bash
python MergePDFs.py --input "C:\Users\Fatin\Documents\PDFs" --output "C:\Users\Fatin\Documents\Merged.pdf"
```

### Web Scraper

**Script Name**: `WebScraper.py`

**Description**: Extracts data from websites based on defined scraping rules.

**Example Usage**

```bash
python WebScraper.py --url "https://example.com" --output "C:\Users\Fatin\Documents\data.json"
```

## Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a Pull Request.

Ensure your code follows PEP 8 guidelines and includes necessary documentation and comments.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Thanks to all contributors and supporters of this project!
- Special thanks to open-source projects like [PyWin32](https://github.com/mhammond/pywin32), [Pillow](https://python-pillow.org/), and [PyPDF2](https://github.com/mstamy2/PyPDF2) for providing essential functionalities.

This `README.md` provides a comprehensive overview of your repository, detailing each tool, installation steps, usage instructions, and other essential information. Adjust the content as needed to better fit the specific tools and functionalities included in your repository.
