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
        #self.note_old = note_old
        #self. note_new = note_new
        self.id = id
        self.dict_notes_tags = dict_notes_tags
        #self.tags_list = tags_list
        #self.tags = {}
        #if tags_list:
        #    self.tags[self.id] = tags_list
    
    def rec_change_note_tag(self, old_phone, new_phone):
        for k,v in enumerate(self.phones):
            if old_phone.value == v.value:
                self.phones[k] = new_phone
                return f"Old phone {old_phone} change to {new_phone}"
        return f"{old_phone} absent for contact {self.note}"
    
    def add_tag(self, tags_list: Tag):
        for i in tags_list:
            if i not in [t for t in self.tags]:
                self.tags.append(i)
                return f"tag {i} add to note {self.note}"
        return f"tag {i} already exists for note {self.note}"
    
    def __str__(self) -> str:
        return f"{self.id}: {', '.join(self.dict_notes_tags)} {', '.join(str (v) for v in self.dict_notes_tags.values())}"
        #return f"{self.id}: {', '.join(str(v) for v in self.dict_notes_tags.values())}"
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
    

dict_notes = AddressNotes()
tags = {}

def no_command(*args):
    return 'unknown_command'

def add_notes(note_tags_str):
    note: str = ''
    tags_list: list = []
    dict_notes_tags: dict = {}
    text = note_tags_str.split()
    for i in text:
        if i.startswith('#'):
            tags_list.append(i)
    for i in text:
        if not i.startswith('#'):
            note += i + ' '
    dict_notes_tags[note] = tags_list
    id: str = dict_notes.get_next()
    tags[id] = tags_list
    rec: RecordNotes = dict_notes.get(str(id))
    if rec:
        return rec.add_tag(tags_list)
    rec = RecordNotes(id, dict_notes_tags)
    return dict_notes.add_record(rec)

def change_note_tag(text):
    search = '#'
    note_new = ''
    tag_new = []
    new_note_tags = {}
    text_split = text.split()
    key = text_split[0]
    text_split.remove(key)
    for i in text_split:
        if i.startswith('#'):
            tag_new.append(i)
    for i in text_split:
        if search not in i:
            note_new += i + ' '
    id: str = dict_notes.get_next()
    id -= 1
    if key == str(id):
        for v in tags.values():
            for tag in v:
                tag_new.append(tag)
    new_note_tags[note_new] = tag_new
    rec: RecordNotes = dict_notes.get(str(key))
    if rec:
        id = key
        rec = RecordNotes(id, new_note_tags)
        return dict_notes.add_record(rec)
    return 'Notes with this number do not exist'

def show_notes(note_tags_str):
    return dict_notes


dict_command = {'add note': add_notes,
                'show note': show_notes,
                'change note': change_note_tag}
#                'change': change_number,
 #               'phone': phone,
  #              'show': show_all,
                
list_end = ['good bye', 'close', 'exit']



def parser_notes(text: str):
    note_tags = text.split()
    command = ''
    note_tags_str: str = ''
    command = command + note_tags[0] + ' '
    note_tags.pop(0)
    command = command + note_tags[0]
    note_tags.pop(0)
    for i in note_tags:
        note_tags_str += i + ' '
    if command in dict_command.keys():
        return dict_command.get(command), note_tags_str
    return no_command, text

def main():
    while True:
        user_input = input('>>>')
        user_input = user_input.lower()
        
        if user_input in list_end:
            print('Good bye!')
            break
        
               
        #if user_input.startswith('add notes'):
        command, note_tags_str= parser_notes(user_input)
        result = command(note_tags_str)
        print(result)
        
        
        
        
if __name__ == '__main__':
    main()