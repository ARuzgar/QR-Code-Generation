import qrcode
import sys
from PIL import Image

# will expand VCard to include more fields
# will add a way to specify the output file name
# will add a way to specify the output file format

# Create a QR code for a phone number
# phone_number: The phone number to encode in the QR code
# name: The name to associate with the phone number
def create_phone_qr(phone_number, name=""):
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:;{name};;;\nFN:{name}\nTEL;TYPE=CELL:{phone_number}\nEND:VCARD"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f"contact_qr_{phone_number}.png")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_phone_qr.py <+phone_number> [name]")
        sys.exit(1)
    
    phone_number = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else ""
    create_phone_qr(phone_number, name)
    print(f"Contact QR code for {name} ({phone_number}) generated successfully.")
