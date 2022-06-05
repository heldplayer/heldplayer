#!/usr/bin/env python3

import os
import pathlib
import subprocess


if __name__ == "__main__":
    for f in (pathlib.Path(f) for f in os.listdir()):
        if f.suffix == ".tex" and f.name[0] != "_":
            subprocess.call(["pdflatex", f])
            # -background white -alpha remove -alpha off
            subprocess.call(["convert", "-background", "white", "-alpha", "remove", "-alpha", "off", "-density", "300", f.with_suffix(".pdf"), f.with_suffix(".png")])
