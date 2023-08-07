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
    def __init__(self, note: Note, tags_list: Tag = None, note_old = None, note_new = None,):
        #self.note_old = note_old
        #self. note_new = note_new
        self.note = note
        self.id: str = id
        self.tags = []
        if tags_list:
            for i in tags_list:
                self.tags.append(i)
    
#    def change_phone(self, old_phone, new_phone):
#        for k,v in enumerate(self.phones):
#            if old_phone.value == v.value:
#                self.phones[k] = new_phone
#                return f"Old phone {old_phone} change to {new_phone}"
#        return f"{old_phone} absent for contact {self.note}"

    def add_tag(self, tags_list: Tag):
        for i in tags_list:
            #if i not in [t.value for t in self.tags]:
            if i not in [t for t in self.tags]:
                self.tags.append(i)
                return f"tag {i} add to note {self.note}"
        return f"tag {i} already exists for note {self.note}"
    
    def __str__(self) -> str:                     
        return f"note: {self.note}{', '.join(str(p) for p in self.tags)} "
        #return f"note: {self.note}: {', '.join(str(p) for p in self.tags)} "
class AddressNotes(UserDict):
    def add_record(self, record: RecordNotes):
        self.data[str(record.note)] = record
        return 'Add success'
    def change_record(self, record: RecordNotes, id_note, new_note):
        #del self.data[old_note.value]
        #print(elf.data)
        self.data[new_note.value] = record
        return 'Change success'
    def get_next(self):
        id=len(self.data)+1
        return  id
    def re_index():
        ...
        
    def __str__(self) -> str:
        #for i in self.data.values:
        return "\n".join(f"id:{r.id}, {r}" for r in self.data.values()) 
        # "\n".join(f"{id:{r.id}, {r}}" for r in self.data.values())
        # "\n".join(f'{str(v)}'  for v in self.data.values())
dict_notes = AddressNotes()
def no_command(*args):
    return 'unknown_command'
def add_notes(note_tags_str):
    note: str = ''
    tags_list: list = []
    text = note_tags_str.split()
    for i in text:
        if i.startswith('#'):
            tags_list.append(i)
    for i in text:
        if not i.startswith('#'):
            note += i + ' '
    rec: RecordNotes = dict_notes.get(str(note))
    if rec:
        return rec.add_tag(tags_list)
    id: str = dict_notes.get_next()
    rec = RecordNotes(note, tags_list, str(id))
    return dict_notes.add_record(rec)


def change_notes(text1: str):
    note_old: str = ''
    note_new: str = ''
    note_list = text1.split()
    search = '@change'
    index = note_list.index(search)
    old_notes = note_list[:index]
    new_notes = note_list[index:]
    for i in old_notes:
        note_old += i + ' '
    new_notes.pop(0)
    for i in new_notes:
        note_new += i + ' '
    old_note = Note(note_old)
    new_note = Note(note_new)
    rec: RecordNotes = dict_notes.get(str(note_old))
    if rec:
        return dict_notes.change_record(rec, old_note, new_note)
def show_notes(note_tags_str):
    return dict_notes
dict_command = {'add note': add_notes,
                'show note': show_notes,
                'change note': change_notes}
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