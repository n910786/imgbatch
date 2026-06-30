"""Image resize engine."""

from PIL import Image
from pathlib import Path
from tqdm import tqdm

SUPPORTED = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff"}


def batch_resize(
    input_dir: Path,
    output_dir: Path,
    width: int | None,
    height: int | None,
    scale: float | None,
    recursive: bool = False,
):
    """Batch resize images."""
    if width is None and height is None and scale is None:
        print("Error: specify --width, --height, or --scale")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    pattern = "**/*" if recursive else "*"
    files = [
        f for f in input_dir.glob(pattern)
        if f.is_file() and f.suffix.lower() in SUPPORTED
    ]

    if not files:
        print(f"No supported images found in {input_dir}")
        return

    for fp in tqdm(files, desc="Resizing", unit="img"):
        img = Image.open(fp)

        if scale:
            new_size = (int(img.width * scale), int(img.height * scale))
        elif width and height:
            new_size = (width, height)
        elif width:
            ratio = width / img.width
            new_size = (width, int(img.height * ratio))
        elif height:
            ratio = height / img.height
            new_size = (int(img.width * ratio), height)
        else:
            continue

        resized = img.resize(new_size, Image.LANCZOS)
        rel = fp.relative_to(input_dir)
        out = output_dir / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        resized.save(out)

    print(f"\nDone. {len(files)} images → {output_dir}")
