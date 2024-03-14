import sys
import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    # 打开PDF文件
    doc = fitz.open(file_path)
    text = ""
    # 遍历每一页
    for page in doc:
        # 提取当前页的文本
        text += page.get_text()
    return text

def save_text_to_file(text, output_file_path):
    # 将文本保存到TXT文件
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# 调用函数并保存结果
if len(sys.argv) > 1:   
    file_path = sys.argv[1]
else:
    file_path = input("Please enter the file path: ")
output_file_path = 'output_text_file.txt'
pdf_text = extract_text_from_pdf(file_path)
save_text_to_file(pdf_text, output_file_path)

print(f"PDF内容已保存到'{output_file_path}'。")
