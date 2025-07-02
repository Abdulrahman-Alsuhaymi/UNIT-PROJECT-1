from pypdf import PdfReader, PdfWriter
from rich.progress import track

def encrypt_pdf():
    filename = input("Enter PDF filename to encrypt: ").strip()
    password = input("Enter password: ").strip()
    output = input("Enter output filename: ").strip()

    reader = PdfReader(filename)
    writer = PdfWriter()

    print("\n🔒 Encrypting pages..\n")

    for page in track(reader.pages, description="Encrypting.."):
        writer.add_page(page)

    writer.encrypt(password)

    with open(output, "wb") as f:
        writer.write(f)

    print(f"✅ Encrypted PDF saved as {output}")


def decrypt_pdf():
    filename = input("Enter encrypted PDF filename: ").strip()
    password = input("Enter password: ").strip()
    output = input("Enter output filename: ").strip()

    reader = PdfReader(filename)
    if not reader.decrypt(password):
        print("❌ Incorrect password.")
        return

    writer = PdfWriter()

    print("\n🔓 Decrypting pages..\n")

    for page in track(reader.pages, description="Decrypting.."):
        writer.add_page(page)

    with open(output, "wb") as f:
        writer.write(f)

    print(f"✅ Decrypted PDF saved as {output}")
