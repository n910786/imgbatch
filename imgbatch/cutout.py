"""Background removal engine."""

import numpy as np
from PIL import Image
from pathlib import Path
from tqdm import tqdm

SUPPORTED = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff"}


def remove_threshold(img: Image.Image, threshold: int = 240) -> Image.Image:
    """Remove white/near-white background by RGB threshold."""
    img = img.convert("RGBA")
    arr = np.array(img)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    mask = (r >= threshold) & (g >= threshold) & (b >= threshold)
    arr[:, :, 3] = np.where(mask, 0, 255)
    return Image.fromarray(arr)


def remove_ai(img: Image.Image) -> Image.Image:
    """Remove background using rembg AI model."""
    try:
        from rembg import remove
        return remove(img)
    except ImportError:
        raise ImportError(
            "rembg not installed. Run: pip install imgbatch[ai]"
        )


def batch_cutout(
    input_dir: Path,
    output_dir: Path,
    threshold: int = 240,
    use_ai: bool = False,
    recursive: bool = False,
):
    """Batch remove backgrounds from images."""
    output_dir.mkdir(parents=True, exist_ok=True)

    pattern = "**/*" if recursive else "*"
    files = [
        f for f in input_dir.glob(pattern)
        if f.is_file() and f.suffix.lower() in SUPPORTED
    ]

    if not files:
        print(f"No supported images found in {input_dir}")
        return

    for fp in tqdm(files, desc="Removing background", unit="img"):
        img = Image.open(fp)
        try:
            result = remove_ai(img) if use_ai else remove_threshold(img, threshold)
        except Exception as e:
            print(f"\n  Failed: {fp.name} - {e}")
            continue

        rel = fp.relative_to(input_dir)
        out = output_dir / rel.with_suffix(".png")
        out.parent.mkdir(parents=True, exist_ok=True)
        result.save(out)

    print(f"\nDone. {len(files)} images → {output_dir}")
