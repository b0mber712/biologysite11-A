from pathlib import Path
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Set your GitHub Pages base URL (no trailing slash):
BASE_URL = "https://<username>.github.io/biology-site"

root = Path(__file__).parent
pages = sorted((root / "pages").glob("*.html"))
out = root / "qr"
out.mkdir(exist_ok=True)

try:
    font = ImageFont.truetype("DejaVuSans.ttf", 12)
except:
    from PIL import ImageFont as _F
    font = _F.load_default()

for p in pages:
    slug = p.stem
    url = f"{BASE_URL}/pages/{slug}.html"
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=8, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    w,h = img.size
    cap_h = 40
    canvas = Image.new("RGB",(w, h+cap_h),"white")
    canvas.paste(img,(0,0))
    draw = ImageDraw.Draw(canvas)
    draw.text((6,h+6), slug, font=font, fill="black")
    canvas.save(out / f"{slug}.png")

print("Done. Updated QR in qr/")