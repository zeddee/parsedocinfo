from pathlib import Path
from parsedocinfo.parse_docinfo import parse, DocInfo
from typing import List

INPUTDIR = ""

def get_rst_from_single_dir(dir_path: str) -> List[Path]:
    return [
      f for 
      f in Path(dir_path).iterdir()
      if Path(dir_path).is_dir()
      ]


def get_rst_from_dirtree(base_dir: str) -> List[Path]:
    assert(Path(base_dir).is_dir()), f"{base_dir} is not a valid directory"
    
    return list(Path(base_dir).glob("**/*.rst"))

if __name__ == "__main__":
    get_rst_from_dirtree(INPUTDIR)