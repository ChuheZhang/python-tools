import fitz  # PyMuPDF

def extract_text_from_pdf_as_html(file_path):
    doc = fitz.open(file_path)
    html = ""
    for page in doc:
        html += page.get_text("html")
    return html

# 将提取的HTML内容保存到文件
def save_html_to_file(html, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(html)

file_path = 'c:/Users/Fatin/Desktop/3月组会/1-s2.0-S2210650222001900-main.pdf'
output_file_path = 'output.html'
pdf_html = extract_text_from_pdf_as_html(file_path)
save_html_to_file(pdf_html, output_file_path)

print(f"PDF内容已保存到'{output_file_path}'，尽量保留了原始格式。")
