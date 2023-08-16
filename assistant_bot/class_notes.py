from collections import UserList
from .class_note_record import Note_Record
import pickle

# from pathlib import Path


class Notes(UserList):
    def __init__(
        self,
        records_per_page: int = 10,
        default_filename: str = "notes",
        id: str = None,
        auto_backup: bool = False,
        auto_restore: bool = False,
        *args,
        **kwargs,
    ):
        self.max_records_per_page = records_per_page
        self.default_filename = default_filename
        self.auto_backup = auto_backup
        self.auto_restore = auto_restore
        self.id = id
        super().__init__(self, *args, **kwargs)

        """
        TODO CHECK IF PRESENT
        """

    def add_record(self, rec: Note_Record) -> bool:
        self.data.append(rec)
        return True

    def search_record_note(self, note_str: str) -> bool:
        ...
        return True

    def search_record_tag(self, tag_str: str) -> bool:
        ...
        return True

    # by index
    def get_record(self, key: int) -> Note_Record:
        return self.data[key]

    # by index
    def remove_record(self, key: int) -> None:
        self.data.pop(key)
        #        del self.data[key]
        return True

    def _gen_filename(self, filename: str) -> str:
        if self.id:
            filename = f"{self.id}_{filename}"
        return filename

    def backup_data(self, version=None, backup: bool = None) -> bool:
        if self.auto_backup or backup:
            if version:
                filename = f"{self.default_filename}_{version}.bin"
            else:
                filename = f"{self.default_filename}.bin"
            with open(self._gen_filename(filename), "wb") as file:
                pickle.dump(self, file)
            return True

    def restore_data(self, version=None, restore: bool = None) -> bool:
        if self.auto_restore or restore:
            if version:
                filename = f"{self.default_filename}_{version}.bin"
            else:
                filename = f"{self.default_filename}.bin"
            try:
                with open(self._gen_filename(filename), "rb") as file:
                    content = pickle.load(file)
                    if type(content) == type(self):
                        self.__dict__.update(content.__dict__)
                        return True
            except Exception:
                return False

    def __str__(self) -> str:
        result = [f"{str(i+1)}: {data}" for i, data in enumerate(self.data)]
        return "\n".join(result)
