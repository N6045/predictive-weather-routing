import sys
from markdown_pdf import MarkdownPdf, Section

def convert_md_to_pdf(md_file, pdf_file):
    pdf = MarkdownPdf(toc_level=0)
    with open(md_file, "r") as f:
        markdown_text = f.read()
        
    pdf.add_section(Section(markdown_text))
    pdf.save(pdf_file)
    print(f"Successfully created {pdf_file}")

if __name__ == "__main__":
    md_path = "/Users/nimish/Desktop/MiniPro/Viva_Questions.md"
    pdf_path = "/Users/nimish/Desktop/MiniPro/Viva_Questions_and_Answers.pdf"
    convert_md_to_pdf(md_path, pdf_path)
