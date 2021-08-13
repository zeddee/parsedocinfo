from pathlib import Path
from parsedocinfo.parse_docinfo import parse, DocInfo
from typing import Dict, List

INPUTDIR = ""

def get_rst_from_single_dir(dir_path: str) -> List[Path]:
    return [
      f for 
      f in Path(dir_path).iterdir()
      if Path(dir_path).is_dir()
      ]


# def get_rst_from_dirtree(base_dir: str) -> List[Path]:
#     """
#     Avoid using. Easier to figure out
#     dirtree when dealing with a single directory
#     a time.
#     """
#     assert(Path(base_dir).is_dir()), f"{base_dir} is not a valid directory"
#     
#     return list(Path(base_dir).glob("**/*.rst"))

def get_doc_info_from_file_list(file_list: List[Path]) -> Dict[str, List[DocInfo]]:
    out = {}
    for f in file_list:
        out[f.stem()] = parse(f)

    return out

if __name__ == "__main__":
    file_list = get_rst_from_single_dir(INPUTDIR)

    aggregated_docinfo_list = get_doc_info_from_file_list(file_list)

    print(aggregated_docinfo_list)