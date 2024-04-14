import qrcode
import sys
from PIL import Image
import urllib.parse

def create_email_qr(to_email, subject, body):
    subject_encoded = urllib.parse.quote(subject)
    body_encoded = urllib.parse.quote(body)
    mailto_link = f"mailto:{to_email}?subject={subject_encoded}&body={body_encoded}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(mailto_link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f"email_qr.png")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python create_email_qr.py <to_email> <subject> <body>")
        sys.exit(1)
    
    to_email = sys.argv[1]
    subject = sys.argv[2]
    body = sys.argv[3]
    create_email_qr(to_email, subject, body)
    print(f"Email QR code generated successfully.")
