from pypdf import PdfReader, PdfWriter

def encrypt_pdf():
    filename = input("Enter PDF filename to encrypt: ").strip()
    password = input("Enter password: ").strip()
    output = input("Enter output filename: ").strip()

    reader = PdfReader(filename)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    with open(output, "wb") as f:
        writer.write(f)

    print(f"Encrypted PDF saved as {output}")

def decrypt_pdf():
    filename = input("Enter encrypted PDF filename: ").strip()
    password = input("Enter password: ").strip()
    output = input("Enter output filename: ").strip()

    reader = PdfReader(filename)
    if not reader.decrypt(password):
        print("Incorrect password.")
        return

    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    with open(output, "wb") as f:
        writer.write(f)

    print(f"Decrypted PDF saved as {output}")