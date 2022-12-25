import fitz
from PIL import Image
import sys

if len(sys.argv) < 2:
    print("Usage: python p2p name.pdf")
    sys.exit()

pdf_file = sys.argv[1]

pdf = fitz.open(pdf_file)

for page in pdf:
    pix = page.get_pixmap(alpha=False)
    output = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    output.save("{}-{}.png".format(pdf_file, page.number), "PNG")

pdf.close()
