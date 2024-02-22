import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

with tempfile.TemporaryDirectory() as tmpdirname:
    subprocess.run(["7z", "x", sys.argv[1], "-o" + tmpdirname])
    tmpdircontents = os.listdir(tmpdirname)
    if len(tmpdircontents) > 1:
        shutil.move(tmpdirname, sys.argv[2] / Path(sys.argv[1]).stem)
    else:
        shutil.move(tmpdirname / Path(tmpdircontents[0]), sys.argv[2])
