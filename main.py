import subprocess

from pathlib import Path
from pdfminer.high_level import extract_text

pdf_search = Path("./files/").glob("*.pdf")

pdf_files = pdf_files = [str(file.absolute()) for file in pdf_search]


for pdf in pdf_files:
        text = extract_text("*.pdf")
        print(text, file=output.txt)
