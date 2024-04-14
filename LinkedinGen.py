import qrcode
import sys
from PIL import Image

def create_linkedin_qr(linkedin_url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(linkedin_url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f"linkedin_qr.png")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_linkedin_qr.py <linkedin_url>")
        sys.exit(1)

    linkedin_url = sys.argv[1]
    create_linkedin_qr(linkedin_url)
    print(f"LinkedIn QR code generated successfully.")
