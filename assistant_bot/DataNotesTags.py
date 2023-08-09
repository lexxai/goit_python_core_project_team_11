from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value
    def __repr__(self) -> str:
        return str(self)
        


class Note(Field):
    ...
    
class Tag(Field):
    ...
    
class RecordNotes:
    def __init__(self, id, dict_notes_tags, tags_list: Tag = None, note_old = None, note_new = None):
        self.id = id
        self.dict_notes_tags = dict_notes_tags
            
    def add_tag(self, tags_list: Tag):
        for i in tags_list:
            if i not in [t for t in self.tags]:
                self.tags.append(i)
                return f"tag {i} add to note {self.note}"
        return f"tag {i} already exists for note {self.note}"
    
    def __str__(self) -> str:
        return f"{self.id}: {', '.join(self.dict_notes_tags)} {', '.join(str (v) for v in self.dict_notes_tags.values())}"
        
class AddressNotes(UserDict):
    def add_record(self, record: RecordNotes):
        self.data[str(record.id)] = record
        return 'Data accepted'
    
    def change_record(self, record: RecordNotes, old_note, new_note):
        del self.data[old_note.value]
        self.data[new_note.value] = record
        return 'Change success'
    
    def get_next(self):
        id=len(self.data)+1
        return  id
    
    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())
    

