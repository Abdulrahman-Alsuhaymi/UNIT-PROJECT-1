from pypdf import PdfReader, PdfWriter
import os

def split_pdf():
    file_name = input("Enter the PDF file name: ").strip()

    if not os.path.isfile(file_name):
        print("File not found.")
        return

    pages_input = input("Enter the page numbers to extract: ").strip()
    folder = input("Enter the folder to save the new PDF: ").strip()

    if not folder:
        print("No folder given.")
        return
    os.makedirs(folder, exist_ok=True)

    try:
        pages = [int(p) for p in pages_input.split(",")]
    except ValueError:
        print("Please enter valid numbers separated by commas.")
        return


    reader = PdfReader(file_name)
    total = len(reader.pages)

    for page in pages:
        page_index = page - 1
        if 0 <= page_index < total:
            writer = PdfWriter()
            writer.add_page(reader.pages[page_index])

            new_file = os.path.join(folder, f"page_{page}.pdf")
            with open(new_file, "wb") as f:
                writer.write(f)

            print("Saved:", new_file)
        else:
            print("Page number is out of range.")


