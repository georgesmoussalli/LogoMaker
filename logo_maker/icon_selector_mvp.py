import json
import os
from pathlib import Path
from typing import Optional

_HERE = Path(os.path.abspath(__file__))
_DIR_DATA = _HERE.parent.parent.joinpath("data")

def find_icon_by_keyword(keyword: str, filename: str) -> Optional[Path]:
    with _DIR_DATA.joinpath(filename).open("r") as f:
        data = json.load(f)

    for element in data:
        if 'keyword1' in element and element['keyword1'] == keyword:
            return _DIR_DATA.joinpath(element['name'])
    return None

