"""Format conversion engine."""

from PIL import Image
from pathlib import Path
from tqdm import tqdm

SUPPORTED = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff"}


def batch_convert(
    input_dir: Path,
    output_dir: Path,
    fmt: str,
    quality: int = 90,
    recursive: bool = False,
):
    """Batch convert images to a target format."""
    output_dir.mkdir(parents=True, exist_ok=True)

    pattern = "**/*" if recursive else "*"
    files = [
        f for f in input_dir.glob(pattern)
        if f.is_file() and f.suffix.lower() in SUPPORTED
    ]

    if not files:
        print(f"No supported images found in {input_dir}")
        return

    for fp in tqdm(files, desc=f"Converting to {fmt.upper()}", unit="img"):
        img = Image.open(fp)
        rel = fp.relative_to(input_dir)
        out = output_dir / rel.with_suffix(f".{fmt}")
        out.parent.mkdir(parents=True, exist_ok=True)

        save_kwargs = {}
        if fmt.lower() in ("jpg", "jpeg"):
            img = img.convert("RGB")
            save_kwargs["quality"] = quality
        elif fmt.lower() == "webp":
            save_kwargs["quality"] = quality

        img.save(out, **save_kwargs)

    print(f"\nDone. {len(files)} images → {output_dir}")
