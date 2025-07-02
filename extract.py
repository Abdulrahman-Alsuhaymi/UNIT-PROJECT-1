import pdfplumber
from rich.progress import track

def extract_text():
    filename = input("Enter PDF filename: ").strip()
    output = input("Enter output text file: ").strip()

    try:
        with pdfplumber.open(filename) as pdf:
            print("\n📝 Extracting text from pages...\n")
            with open(output, "w", encoding="utf-8") as out:
                for page in track(pdf.pages, description="Extracting.."):
                    text = page.extract_text()
                    if text:
                        out.write(text)

        print(f"✅ Extracted text saved to {output}")
    
    except FileNotFoundError:
        print("❌ File not found.")
