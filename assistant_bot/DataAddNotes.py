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
    
class Note_Record:
    def __init__(self, note: Note, tag: Tag = None):
        self.note = note
        self.tags = []
        if tag:
            self.tags.append(tag)
    
    '''def change_phone(self, old_phone, new_phone):
        for k,v in enumerate(self.phones):
            if old_phone.value == v.value:
                self.phones[k] = new_phone
                return f"Old phone {old_phone} change to {new_phone}"
        return f"{old_phone} absent for contact {self.note}"'''
    
    '''def add_tag(self, tag: Tag):
        if tag not in [p.value for p in self.tags]:
            self.tags.append(tag)
            return f"tag {tag} add to notes {self.note}"
        return f"tag {tag} already exists for notes {self.note}"'''
    
    def __str__(self) -> str:
        return f"{self.note}: {', '.join(str(p) for p in self.tags)}"
    
class AddressNotes(UserDict):
    def add_record(self, record: Note_Record):
        self.data[str(record.note)] = record
        return 'Add success'
    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())
    
dict_notes = AddressNotes()


def no_command(*args):
    return 'unknown_command'

def handler_add_note(self, *args) -> str:
        result = None
        note_list: list = []
        note_str:str = None
        tags: list = []
        for arg in args:
            if arg.startswith('#'):
                tag_str:str = str(arg[1:]).strip()
                tags.append(Tag(tag_str))
            else:
                note_list.append(arg)
        if note_list:
            note_str = " ".join(note_list)
        
        note_rec = Note_Record( Note(note_str), tags )
        result = self.a_notes.add_record(note_rec)


dict_command = {'add note': handler_add_note}
 #               'show notes': show_notes}
 #               'change notes': change_notes}
#                'change': change_number,
 #               'phone': phone,
  #              'show': show_all,
                
list_end = ['good bye', 'close', 'exit']



def parser_notes(text: str) -> tuple[callable, tuple[str]]:
    command = ''
    tags_text = ''
    notes_text = ''
    text1 = text.split()
    text2 = text.split()
    command = command + text2[0] + ' '
    text2.pop(0)
    command = command + text2[0]
    text2.pop(0)
    search = '#'
    if command in dict_command.keys():
        if command == 'change notes':
            old_notes_str = ''
            new_notes_str = ''
            search = '@change'
            index = text2.index(search)
            old_notes = text2[:index]
            new_notes = text2[index:]
            for i in old_notes:
                old_notes_str += i + ' '
            new_notes.pop(0)
            for i in new_notes:
                new_notes_str += i + ' '
            return dict_command.get(command), old_notes, new_notes
        if command == 'add notes':    
            for i in text1:
                if search in i:
                    tags_text += i + ' '
                    text2.remove(i)
            for i in text2:
                notes_text += i + ' '
            return dict_command.get(command), notes_text, tags_text
        return dict_command.get(command), notes_text, tags_text
    return no_command, text, text

def main():
    while True:
        user_input = input('>>>')
        user_input = user_input.lower()
        
        if user_input in list_end:
            print('Good bye!')
            break
        
               
        #if user_input.startswith('add notes'):
        command, notes_text,  tags_list= parser_notes(user_input)
        result = command(notes_text,  tags_list)
        print(result)
        
        
        
        
if __name__ == '__main__':
    main()
    
#wefwef