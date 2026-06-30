# imgbatch

[![CI](https://github.com/n910786/imgbatch/actions/workflows/ci.yml/badge.svg)](https://github.com/n910786/imgbatch/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/imgbatch.svg)](https://badge.fury.io/py/imgbatch)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Batch image processing CLI** — cutout, convert, resize. Built with Python.

## Features

- **Cutout** — Remove white/green background via threshold algorithm or AI (rembg)
- **Convert** — Batch convert between PNG, JPG, WebP, BMP, TIFF
- **Resize** — Scale by dimensions or factor, preserves aspect ratio
- **Recursive** — Process entire folder trees
- **Progress bar** — Live feedback with tqdm

## Installation

```bash
pip install imgbatch
```

For AI-powered background removal:
```bash
pip install imgbatch[ai]
```

## Quick Start

```bash
# Remove white background from all images
imgbatch cutout ./photos -o ./photos_bg

# Convert JPGs to PNG
imgbatch convert ./photos -f png -o ./photos_png

# Resize all images to 50%
imgbatch resize ./photos -s 0.5 -o ./photos_small

# AI cutout (requires imgbatch[ai])
imgbatch cutout ./photos --ai
```

## Commands

### `cutout` — Background Removal

```
imgbatch cutout INPUT_DIR [OPTIONS]

Options:
  -o, --output-dir PATH    Output directory (default: INPUT_DIR_cutout)
  -t, --threshold INT      White threshold 0-255 (default: 240)
  --ai                     Use rembg AI engine
  -r, --recursive          Process subdirectories
```

### `convert` — Format Conversion

```
imgbatch convert INPUT_DIR [OPTIONS]

Options:
  -o, --output-dir PATH    Output directory
  -f, --format [png|jpg|jpeg|webp|bmp|tiff]  Target format
  -q, --quality INT        Quality for JPG/WebP (default: 90)
  -r, --recursive          Process subdirectories
```

### `resize` — Image Resize

```
imgbatch resize INPUT_DIR [OPTIONS]

Options:
  -o, --output-dir PATH    Output directory
  -w, --width INT          Target width
  -H, --height INT         Target height
  -s, --scale FLOAT        Scale factor (e.g., 0.5)
  -r, --recursive          Process subdirectories
```

## License

MIT © n910786
