from pypdf import PdfReader, PdfWriter
import os

def split_pdf():
    # Ask for the PDF file name
    file_name = input("Enter the PDF file name: ").strip()

    # Check if the file exists
    if not os.path.isfile(file_name):
        print("File not found.")
        return

    # Ask for the page number
    try:
        page = int(input("Enter the page number to extract: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return

    # Ask for the output folder
    folder = input("Enter the folder to save the new PDF: ").strip()

    # Make the folder if it doesn't exist
    if not folder:
        print("No folder given.")
        return
    os.makedirs(folder, exist_ok=True)

    # Open the PDF and check the page range
    reader = PdfReader(file_name)
    total = len(reader.pages)
    page_index = page - 1

    # If the page is valid, write it to a new file
    if 0 <= page_index < total:
        writer = PdfWriter()
        writer.add_page(reader.pages[page_index])

        new_file = os.path.join(folder, f"page_{page}.pdf")
        with open(new_file, "wb") as f:
            writer.write(f)

        print("Saved:", new_file)
    else:
        print("Page number is out of range.")


