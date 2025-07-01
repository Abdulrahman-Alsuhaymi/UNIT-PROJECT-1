from merge import merge_pdfs
from split import split_pdf
from encrypt import encrypt_pdf, decrypt_pdf
from extract import extract_text
def main():
    print(" Welcome to PDFSwissKnife")
    while True:
        print("\nChoose an option: ")
        print("1 - Merge PDFs ")
        print("2 - Split PDFs ")
        print("3 - Encrypt PDF ")
        print("4 - Decrypt PDF ")
        print("5 - Extract text ")

        print("q - Exit ")
        choice = input(">> ").strip()

        if choice == "1":
            merge_pdfs()
        elif choice == "2":
            split_pdf()
        elif choice == "3":
            encrypt_pdf()
        elif choice == "4":
            decrypt_pdf()
        elif choice == "5":
            extract_text()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid input")
main()