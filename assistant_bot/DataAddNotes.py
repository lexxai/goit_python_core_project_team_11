from collections import UserDict
from datetime import datetime
import re, pickle


FILE_PATH = "./notes.bin"



class Date:
    def __init__(self):
        self.current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def __str__(self):
        return f"Created at: {self.current_datetime}"
    
    def __repr__(self):
        return self
    

class Note():
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return str(self.value)
    
class Tag():
    def __init__(self, value=''):
        self.value = value
        
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return str(self.value)
    
class Note_Record:
    def __init__(self, index, note: Note, creation_date: Date, tag: Tag = None):
        self.index = index
        self.note = note
        self.creation_date = creation_date
        self.tags = tag if tag is not None else []
        
    def __str__(self) -> str:
        return f"{self.note}\nTags#: {self.tags}\n{self.creation_date}\n"
    
    def __repr__(self) -> str:
        return str(self)
    
class Notes(UserDict):
    def add_record(self, record: Note_Record):
        self.data[record.index] = record
    
    def change_note(self, record: Note_Record):
        self.data[self.index] = record
                
    def delete_note(self, index):
        removed_note = self.data.pop(index)
        for key in list(self.data.keys()):
            if int(key) > int(index):
                self.data[str(int(key) - 1)] = self.data.pop(key)
        return removed_note
    
    def sort_notes(self, type):
        ...
    
    def search_notes(self, search_str):
        ...
        
    def serialize(self, file_path):
        with open(file_path, "wb") as file:
            pickle.dump(self.data, file)

    def deserialize(self, file_path):
        with open(file_path, "rb") as file:
            self.data = pickle.load(file)

class Iterator:
    def __init__(self, notes):
        self.notes = notes
        self.current_value = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_value < len(self.notes):
            index = list(self.notes.data.keys())[self.current_value]
            record = list(self.notes.data.values())[self.current_value]
            self.current_value += 1
            return f"{index}. {record}"
        raise StopIteration("End")
    
notes = Notes()


def no_command(*args):
    return 'unknown_command'

def add_note(*args) -> str:
        if not notes:       
            index = 1
        else:
            max_key = max(notes.data.keys(), key=int)
            index = int(max_key) + 1
        note = Note(input('Enter note:\n'))
        tags = input('Enter Tags#:\n')
        tags = [Tag(tag) for tag in tags.split(' ')]
        date = Date()
        record = Note_Record(index, note, date, tags)
        notes.add_record(record)
        notes.serialize(FILE_PATH)
        return f'{index}. {record}'
    
        
def show_notes(*args):
    if not notes:
        return 'No notes in notebook'
    else:
        iterator = Iterator(notes)
        for record in iterator:
            print(record)
            try:
                input("Press 'Enter' to continue\n")
            except KeyboardInterrupt:
                break
    return "End\n"
        
def change_note(index):
    index = int(index[0])
    if notes.data[index]:
        date = Date()
        record = notes.data[index]
        note = record.note
        tags = record.tags
        type =input('Press "1" to edit notes, "2" - to edit Tags#: ')
        if type == '1':
            note = Note(input(f'Current record({record.note}): '))
        elif type == '2':
            tags = input(f'Current #Tags({record.tags}): ')
            tags = [Tag(tag) for tag in tags.split(' ')]
        else:
            print('Wrong choise')
        record = Note_Record(index, note, date, tags)
        notes.add_record(record)
        notes.serialize(FILE_PATH)
        return f'{index}. {record}'
    else:
        return f'No record with {index} index'
        
def delete_note(index):
    index = int(index[0])
    if notes.data[index]:
        record = notes
    return f'Note:\n{index}. {record.delete_note(index)}was removed'

def sort_notes(type):
    ...

def search_notes(search_str):
    ...


dict_command = {'add notes': add_note,
               'show notes': show_notes,
               'change notes': change_note,
               'delete notes': delete_note,
               'sort notes': sort_notes,
               'search notes': search_notes}
                
list_end = ['good bye', 'close', 'exit']

def parse_input(command_line: str) -> tuple[object, list]:
    line: str = command_line.lower().lstrip()
    match = re.search(r'^(\w+\s+\w{5})\s*(.*)', line,)
    user_command, args = match.group(1), match.group(2).split()
    if user_command in dict_command.keys():
        return dict_command[user_command], args
    else:
        return 'Wrong command'


def main():
    try:
        notes.deserialize(FILE_PATH)
    except FileNotFoundError:
        print("No file found. New notebook was created.")
    
    
    while True:
        user_input = input('>>>')
        user_input = user_input.lower()
        
        if user_input in list_end:
            print('Good bye!')
            break
        command, args = parse_input(user_input)
        # try:
        result = command(args)
        print(result)
        # except KeyError:
            # print('Wrong command2')
        

# def api(*args):
#     print(f"DataAddNote.api : args = {args}")
#     result=parser_args(*args)
#     return f"DataAddNote API DONE {result=}"
        
        
        
if __name__ == '__main__':
    main()