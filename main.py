from merge import merge_pdfs
from split import split_pdf
def main():
    print(" Welcome to PDFSwissKnife")
    while True:
        print("\nChoose an option: ")
        print("1 - Merge PDFs ")
        print("1 - Split PDFs ")
        print("q - Exit ")
        choice = input(">> ").strip()

        if choice == "1":
            merge_pdfs()
        elif choice == "2":
            split_pdf()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid input")
main()