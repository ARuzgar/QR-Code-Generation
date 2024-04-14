import qrcode
import sys
from PIL import Image

def create_email_qr(email_address):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    mailto_link = f"mailto:{email_address}"
    qr.add_data(mailto_link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f"email_qr.png")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_email_qr.py <email_address>")
        sys.exit(1)
    
    email_address = sys.argv[1]
    create_email_qr(email_address)
    print(f"Email QR code for {email_address} generated successfully.")
