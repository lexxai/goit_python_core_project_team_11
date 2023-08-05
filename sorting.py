import sys
from pathlib import Path
import uuid
import shutil

from normalize import normalize


CATEGORIES = {"Audio": [".mp3", ".aiff", ".amr", ".ogg", ".wav"],
              "Documents": [".doc", ".docx", ".rtf", ".xlsx", ".pptx", ".txt", ".pdf"],
              "Images":[".jpeg", ".png", ".jpg", ".svg"],
              "Video":[".avi", ".mp4", ".mov", ".mkv",],
              "Archives":[".zip", ".gz", ".tar"]}

list_know_ext = []
list_not_know_ext = []


def move_file(file: Path, root_dir: Path, categorie: str) -> None:
    target_dir = root_dir.joinpath(categorie)
    if not target_dir.exists():
        target_dir.mkdir()
    new_name = target_dir.joinpath(f"{normalize(file.stem)}{file.suffix}")
    if new_name.exists():
       new_name = new_name.with_name(f"{new_name.stem}-{uuid.uuid4()}{file.suffix}")
    file.rename(new_name)
    

def get_categories(file: Path) -> str:
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            if ext not in list_know_ext:
                list_know_ext.append(ext)
            return cat
    if ext not in list_not_know_ext:
        list_not_know_ext.append(ext)
    return "Other"


def sort_folder(path: Path) -> None:
    for item in path.glob("**/*"):
        if item.is_file():
            if str(item).find('Archives') == -1 and str(item).find('Video') == -1 and str(item).find('Audio') == -1 and str(item).find('Documents') == -1 and str(item).find('Images') == -1:
                cat = get_categories(item)
                move_file(item, path, cat)

def delete_emtpy_dirs(path: Path) -> None:
    for item in path.glob("**/*"):
        if item.is_dir():
            delete_emtpy_dirs(item)
            if len(list(item.iterdir())) == 0:
                item.rmdir()

def upack_archive(path: Path) -> None:
    p = Path(path, "Archives")
    for item in p.glob("*"):
        if item.suffix == ".zip" or item.suffix == ".gz" or item.suffix == ".tar":  
            target_dir = p.joinpath(item.stem)
            if not target_dir.exists():
                target_dir.mkdir()
            shutil.unpack_archive(item, target_dir)
            item.unlink()

def list_folder(path: Path) -> None:
    list_all = "\nAll found files have been sorted:\n"
    for item in path.glob("**/*"):
        if item.is_dir():
            list_all += f"\nfolder: {item}:\n"
            for files in item.glob("**/*"):
                if files.is_dir():
                    list_all += f"subfolder: {files.stem}:\n"
                if files.is_file():
                    list_all += f"{files.stem}{files.suffix}\n"
    return list_all


def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"
    
    if not path.exists():
        return f"Folder with path {path} dos`n exists."
    
    sort_folder(path)
    delete_emtpy_dirs(path)
    upack_archive(path)
    print(list_folder(path))
    print(f"\nFound known file extensions: {list_know_ext}")
    print(f"\nFound not known file extensions: {list_not_know_ext}")
    
    return "\nFinish"


if __name__ == "__main__":
    print(main())