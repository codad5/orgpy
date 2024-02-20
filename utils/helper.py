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


def is_dir_exists(dir) -> bool:
    return os.path.isdir(dir)


def move_by_ext(path, ext_to_path_mapping=None):
    if ext_to_path_mapping is None:
        ext_to_path_mapping = dict()
    files = get_all_file_recursively(path)
    for file in files:
        file = Path(file)
        if file.suffix in ext_to_path_mapping:
            src = os.path.join(path, file)
            # move to the new directory created inside the src directory
            dest = os.path.join(path, ext_to_path_mapping[file.suffix])
        else:
            default = ext_to_path_mapping["default"]
            src = os.path.join(path, file)
            dest = os.path.join(path, default)

        if not os.path.exists(dest):
            os.makedirs(dest)
        os.rename(src, os.path.join(dest, file))
        print(f"Moved {src} to {dest}")
    print("All files moved successfully")

