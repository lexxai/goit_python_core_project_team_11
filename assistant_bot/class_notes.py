from collections import UserList
from .class_note_record import Note_Record
from .class_fields import Note, Tag
import pickle
#from pathlib import Path


class Notes(UserList):

    def __init__(self, records_per_page: int = 10,
                 default_filename: str = "notes",
                 id: str = None,
                 auto_backup: bool = False,
                 auto_restore: bool = False,
                 *args, **kwargs):
        self.max_records_per_page = records_per_page
        self.default_filename = default_filename
        self.auto_backup = auto_backup
        self.auto_restore = auto_restore
        self.id = id
        self.tags = list()
        super().__init__(self, *args, **kwargs)


        """
        TODO CHECK IF PRESENT
        """
    def add_record(self, rec: Note_Record) -> bool:
        for i, rec_val in enumerate(self.data):
            #print(f"{i=}, {str(rec_val)}")
            if rec_val.note.value == rec.note.value:
                return True
        self.data.append(rec)
        #idx = len(self.data)-1
        return True


    def index_tag(self, tag: Tag) -> int:
        for idx, tag_val in enumerate(self.tags,0):
            print(f"{idx=}, {str(tag_val)}")
            if tag_val.value == tag.value:
                print(f"add_tag {tag=}, found index: {idx}")
                return idx
        return -1      

    def tag_by_index(self, idx: int) -> Tag:
        if idx < len(self.tags):
            return self.tags[idx]

    def tag_list_by_index(self, list_index: list[int]) -> Tag:
        result = []
        for tag_idx in  list_index:
            result.append(self.tag_by_index(tag_idx))
        return result




    def add_tag(self, tag: Tag) -> None:
        idx = self.index_tag(tag)
        if idx == -1:
            self.tags.append(tag)
            idx = len(self.tags)-1
            print(f"add_tag {tag=}, new index: {idx}")
        return idx
 

    def search_record_note(self, note_str: str) -> bool:
        for i, rec_val in enumerate(self.data):
            note = str(rec_val.note.value)
            if note.find(note_str) != -1:
                return i
        return False  

    def search_record_tag(self, tag_str: str ) -> bool:
        ...
        return True    

    #by index
    def get_record(self, key: int) -> Note_Record:
        return self.data[key]

    #by index
    def remove_record(self, key :int) -> None:
        self.data.pop(key)
#        del self.data[key]
        return True

    def _gen_filename(self, filename: str) -> str:
        if self.id:
            filename = f"{self.id}_{filename}"
        return filename      


    def backup_data(self, version=None, backup:bool = None) -> bool:
        if self.auto_backup or backup:
            if version:
                filename = f"{self.default_filename}_{version}.bin"
            else:
                filename = f"{self.default_filename}.bin"
            with open(self._gen_filename(filename), "wb") as file:
                pickle.dump(self, file)
            return True


    def restore_data(self, version=None, restore:bool = None) -> bool:
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
        result = []
        for i, data in enumerate(self.data):
            note = data.note
            tags = self.tag_list_by_index(data.tags)
            tags_fmt = ", ".join([ f"#{tag}" for tag in tags ])
            result.append(f"{str(i+1)}: {note}, {tags_fmt}")
        # result = [ f"{str(i+1)}: {data}" for i, data in enumerate(self.data) ]
        return "\n".join(result)

    # def __iter__(self):
    #     self._page_pos = 0
    #     return self


    # def __next__(self) -> str:
    #     page = []
    #     for i, rec_val in enumerate(self.data):
    #         #print(i, self._page_pos, self._per_page, page)
    #         if self._page_pos < self._per_page:
    #             page.append(f"{str(i+1)}: {rec_val}")
    #             self._page_pos += 1
    #         else:
    #             return "\n".join(page)
    #             print("A Y")
    #             page = []
    #             self._page_pos = 0
    #     self._page_pos = 0
    #     raise StopIteration

    # def __next__(self) -> list[Record]:
    #     if self._page_pos < len(self.data.keys()):
    #         result = []
    #         idx_min = self._page_pos
    #         idx_max = self._page_pos + self.max_records_per_page
    #         #print(f"__next__ {idx_min=}, {idx_max=}")
    #         keys = list(self.data)[idx_min:idx_max]
    #         for key in keys:
    #             result.append(self.data[key])
    #         self._page_pos += self.max_records_per_page
    #         return result
    #     self._page_pos = 0
    #     raise StopIteration

        
