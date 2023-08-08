import os
import fitz

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text("text")

    pdf_document.close()
    return text

def main():
    pdf_folder = "./files"
    output_folder = "./output"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for pdf_filename in os.listdir(pdf_folder):
        if pdf_filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, pdf_filename)
            text = extract_text_from_pdf(pdf_path)

            text_filename = os.path.splitext(pdf_filename)[0] + ".txt"
            text_path = os.path.join(output_folder, text_filename)

            with open(text_path, "w", encoding="utf-8") as text_file:
                text_file.write(text)

            print(f"Extracted text from {pdf_filename} and saved as {text_filename}")

if __name__ == "__main__":
    main()
