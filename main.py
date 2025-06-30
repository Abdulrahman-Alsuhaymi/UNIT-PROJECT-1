from merge import merge_pdfs
from split import split_pdf
def main():
    print(" Welcome to PDFSwissKnife")
    while True:
        print("\nCommands: merge = 1 | split = 2 ")
        cmd = input(">> ").strip().lower()

        if cmd == "1":
            merge_pdfs()
        elif cmd == "2":
            split_pdf()
main()