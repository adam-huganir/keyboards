import datetime
import glob
import os
import shutil
import subprocess
import sys

drive = sys.argv[1] if len(sys.argv) > 1 else "J:\\"


def copy_file(filename):
    remote_file = get_remote_file(filename)
    if filename in {"boot.py", "code.py"}:
        print(f"Copying {filename} to {drive}")
        shutil.copy(filename, drive)
        return
    print("Compiling and copying " + filename)
    if compile_file(filename) != 0:
        print("Compilation failed, not copying")
        return
    mpy_file = os.path.splitext(filename)[0] + ".mpy"
    with open(remote_file, "wb") as fp:
        fp.write(open(mpy_file, "rb").read())
    os.remove(mpy_file)


def compile_file(f):
    comp = subprocess.run(
        [
            "mpy-cross",
            "-v",
            f,
        ],
        capture_output=True,
    )
    return comp.returncode


def get_remote_file(f):
    p = os.path.join(drive, f)
    return p if f in {"boot.py", "code.py"} else os.path.splitext(p)[0] + ".mpy"


for f in glob.glob("*", recursive=False):
    if f.startswith("kmk\\"):
        continue
    if f == "sync.py":
        continue
    if not f.endswith(".py"):
        continue
    fr = get_remote_file(f)

    s_local = os.stat(f)
    if not os.path.exists(fr):
        print(f"Not found, copying {f} to {drive}")
        copy_file(f)
        continue
    s_remote = os.stat(fr)
    dtl = datetime.datetime.fromtimestamp(s_local.st_mtime)
    dtr = datetime.datetime.fromtimestamp(s_remote.st_mtime)
    if dtr < dtl:
        print(f"File modified, copying {f} to {drive}")
        copy_file(f)
        continue
    print(f"File not modified, skipping {f}")
