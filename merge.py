from pypdf import PdfReader, PdfWriter
from rich.progress import track

def merge_pdfs():
    files = input("Enter PDF filenames : ").split(",")
    output = input("Enter output filename: ").strip()

    writer = PdfWriter()
    for f in track(files, description="Merging PDFs.."):
        try:
            reader = PdfReader(f.strip())
            for page in reader.pages:
                writer.add_page(page)
        except Exception as e:
            print(f"Failed to process: {f}  {e}")

    with open(output, "wb") as out_file:
        writer.write(out_file)
    
    print(f"✅ Merged PDF saved as {output}")
    


