# Helpers shared by the animation scripts in this folder.
# drawbot-skia can't save GIFs, so the pages are saved as PNG frames,
# joined into a GIF with Pillow, then compressed with gifsicle
# (brew install gifsicle) when it is installed.

import argparse
import pathlib
import shutil
import subprocess
import tempfile

from drawbot_skia.drawbot import saveImage
from PIL import Image


def parse_output(default):
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", metavar="GIF", default=default)
    return parser.parse_args().output


def save_gif(path, frame_duration=1 / 24, colors=16):
    path = pathlib.Path(path)
    with tempfile.TemporaryDirectory(prefix="firjar-gif-") as tmp:
        saveImage(str(pathlib.Path(tmp) / "frame.png"))
        frames = sorted(
            pathlib.Path(tmp).glob("frame_*.png"),
            key=lambda p: int(p.stem.split("_")[1]),
        )
        images = [Image.open(f).convert("RGB") for f in frames]
        images[0].save(
            path,
            save_all=True,
            append_images=images[1:],
            duration=round(frame_duration * 1000),
            loop=0,
        )
    if shutil.which("gifsicle"):
        subprocess.run(
            ["gifsicle", "-b", "-O3", "--colors", str(colors), str(path)],
            check=True,
        )
    else:
        print("gifsicle not found, GIF left uncompressed (brew install gifsicle)")
