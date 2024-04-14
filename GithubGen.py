import qrcode
import sys
from PIL import Image

def create_github_qr(github_url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(github_url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f"github_qr.png")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_github_qr.py <github_url>")
        sys.exit(1)
    
    github_url = sys.argv[1]
    create_github_qr(github_url)
    print(f"GitHub QR code generated successfully.")
