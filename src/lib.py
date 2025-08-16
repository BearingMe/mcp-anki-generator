import os
from typing import Optional


def read_as_str(relative_path: str) -> Optional[str]:
    full_path = os.path.abspath(relative_path)

    try:
        with open(full_path, "r") as file:
            return file.read()

    except FileNotFoundError as err:
        print(f"FileNotFoundError: {err}")
        print(f"Full path attempted: {full_path}")
