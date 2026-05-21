"""
One-off image optimizer for the David + Gracie homepage hero photo.
Produces responsive JPG + WebP renditions at three sizes, strips EXIF,
and reports the output sizes so we can confirm mobile-friendly weight.
"""

from PIL import Image
from pathlib import Path
import sys

SRC = Path(r"C:\Users\Vetpe\OneDrive\Docusign documents\Desktop\Fianl pics\david-gracie-bennettvet.com")
OUT_DIR = Path(r"C:\Users\Vetpe\OneDrive\Documents\Bennettvet-newsite\images")
BASENAME = "david-gracie"

# Three widths: large (desktop hero), medium (tablet / smaller layouts),
# small (mobile). The browser picks whichever matches the layout slot.
WIDTHS = [
    ("1600", 1600),
    ("800", 800),
    ("400", 400),
]

JPG_QUALITY = 82       # visually lossless for photos at this density
WEBP_QUALITY = 80      # WebP needs less to look the same

def main() -> int:
    if not SRC.exists():
        print(f"ERROR: source not found: {SRC}", file=sys.stderr)
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with Image.open(SRC) as im:
        # Convert to RGB (handles PNG with alpha — flattens against white)
        if im.mode in ("RGBA", "LA", "P"):
            bg = Image.new("RGB", im.size, (255, 255, 255))
            if im.mode == "P":
                im = im.convert("RGBA")
            bg.paste(im, mask=im.split()[-1] if im.mode in ("RGBA", "LA") else None)
            im = bg
        else:
            im = im.convert("RGB")

        src_w, src_h = im.size
        print(f"Source: {src_w}x{src_h}, {SRC.stat().st_size // 1024} KB ({SRC.suffix or 'no ext'})")

        for label, target_w in WIDTHS:
            if target_w >= src_w:
                resized = im.copy()
            else:
                aspect = src_h / src_w
                target_h = int(round(target_w * aspect))
                resized = im.resize((target_w, target_h), Image.LANCZOS)

            jpg_path = OUT_DIR / f"{BASENAME}-{label}.jpg"
            webp_path = OUT_DIR / f"{BASENAME}-{label}.webp"

            resized.save(
                jpg_path,
                "JPEG",
                quality=JPG_QUALITY,
                optimize=True,
                progressive=True,
            )
            resized.save(
                webp_path,
                "WEBP",
                quality=WEBP_QUALITY,
                method=6,
            )

            jpg_kb = jpg_path.stat().st_size // 1024
            webp_kb = webp_path.stat().st_size // 1024
            print(f"  {label:>5}w  JPG {jpg_kb:>4} KB   WebP {webp_kb:>4} KB   -> {resized.size}")

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
