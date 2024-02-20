import os
from pathlib import Path


def get_all_file_recursively(path=".", recursive=False) -> list[str]:
    files = []
    if not recursive:
        for file in os.listdir(path):
            if not os.path.isfile(os.path.join(path, file)):
                continue
            files.append(file)
    else:
        for root, dirs, files in os.walk("."):
            files = files
    return files


def get_all_existing_ext_in_dir(path=".", recursive=False):
    files = get_all_file_recursively(path, recursive)
    extensions = set()
    for i in files:
        file = Path(os.path.join(path, i))
        extensions.add(file.suffix)
    return extensions
