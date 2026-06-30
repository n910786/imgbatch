"""imgbatch CLI - batch image processing tool."""

import click
from pathlib import Path
from .cutout import batch_cutout
from .convert import batch_convert
from .resize import batch_resize


@click.group()
@click.version_option()
def main():
    """imgbatch - Batch image processing toolkit."""
    pass


@main.command()
@click.argument("input_dir", type=click.Path(exists=True))
@click.option("-o", "--output-dir", default=None, help="Output directory (default: input_dir_bg)")
@click.option("-t", "--threshold", default=240, show_default=True, help="White threshold (0-255)")
@click.option("--ai", is_flag=True, help="Use rembg AI engine instead of threshold")
@click.option("-r", "--recursive", is_flag=True, help="Process subdirectories")
def cutout(input_dir, output_dir, threshold, ai, recursive):
    """Remove white/green background from images.
    
    INPUT_DIR: directory containing images to process.
    """
    import os
    out = output_dir or os.path.join(input_dir, "_cutout")
    batch_cutout(Path(input_dir), Path(out), threshold, ai, recursive)


@main.command()
@click.argument("input_dir", type=click.Path(exists=True))
@click.option("-o", "--output-dir", default=None, help="Output directory")
@click.option("-f", "--format", "fmt", default="png", show_default=True, 
              type=click.Choice(["png", "jpg", "jpeg", "webp", "bmp", "tiff"]))
@click.option("-q", "--quality", default=90, show_default=True, help="JPEG/WebP quality")
@click.option("-r", "--recursive", is_flag=True, help="Process subdirectories")
def convert(input_dir, output_dir, fmt, quality, recursive):
    """Convert images to another format."""
    import os
    out = output_dir or os.path.join(input_dir, f"_converted_{fmt}")
    batch_convert(Path(input_dir), Path(out), fmt, quality, recursive)


@main.command()
@click.argument("input_dir", type=click.Path(exists=True))
@click.option("-o", "--output-dir", default=None, help="Output directory")
@click.option("-w", "--width", type=int, default=None, help="Target width (preserves ratio if only one given)")
@click.option("-H", "--height", type=int, default=None, help="Target height")
@click.option("-s", "--scale", type=float, default=None, help="Scale factor (e.g. 0.5 = half)")
@click.option("-r", "--recursive", is_flag=True, help="Process subdirectories")
def resize(input_dir, output_dir, width, height, scale, recursive):
    """Resize images by dimensions or scale factor."""
    import os
    out = output_dir or input_dir  # in-place if no output-dir
    batch_resize(Path(input_dir), Path(out), width, height, scale, recursive)
