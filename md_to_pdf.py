import sys
from markdown_pdf import MarkdownPdf, Section

def convert_md_to_pdf(md_file, pdf_file):
    pdf = MarkdownPdf()
    with open(md_file, "r") as f:
        markdown_text = f.read()
        
    pdf.add_section(Section(markdown_text))
    pdf.save(pdf_file)
    print(f"Successfully created {pdf_file}")

if __name__ == "__main__":
    md_path = "/Users/nimish/.gemini/antigravity/brain/ca0b4445-d323-41d5-9981-4e79a410df91/Presentation_Script.md"
    pdf_path = "/Users/nimish/Desktop/MiniPro/Final_Complete_Presentation_Script.pdf"
    convert_md_to_pdf(md_path, pdf_path)
