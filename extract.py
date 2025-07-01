import pdfplumber

def extract_text():
    filename = input("Enter PDF filename: ").strip()
    output = input("Enter output text file: ").strip()

    with pdfplumber.open(filename) as pdf:
        with open(output, "w", encoding="utf-8") as out:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    out.write(text)
                    

    print(f"Extracted text saved to {output}")