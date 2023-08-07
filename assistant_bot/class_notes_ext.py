from collections import UserDict
from datetime import datetime 
import re, pickle


FILE_PATH = "./assistant_bot/notes.bin"

class Date:
    def __init__(self):
        self.current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    def __str__(self):
        return f"Created at: {self.current_datetime}"
    
    def __repr__(self):
        return str(self)
    

class Note():
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)
    
    
class Tag():
    def __init__(self, value=''):
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
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
    
    def search(self, search_str, category):
        results = {}
        for key, record in self.data.items():
            if category == 1:
                if re.search(search_str, str(record.note)):
                    results[key] = record
            elif category == 2:
                if any(search_str in str(tag) for tag in record.tags):
                    results[key] = record
        return results
    
    def sort(self, category):
        if category == '1': #Datetime
            results = sorted(notes.data.items(), key=lambda item: str(item[1].creation_date))
        elif category == '2': #Index
            results = sorted(notes.data.items(), key=lambda item: item[1].index)
        elif category == '3': #Tags
            results = sorted(notes.data.items(), key=lambda item: [tag.value for tag in item[1].tags])
        return results
        
    # def serialize(self, file_path):
    #     with open(file_path, "wb") as file:
    #         pickle.dump(self.data, file)

    # def deserialize(self, file_path):
    #     with open(file_path, "rb") as file:
    #         self.data = pickle.load(file)


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


# def no_command(*args):
#     return 'unknown_command'


def add_note(*args) -> str:
    print(f"add_note {__name__} {args=}")
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
    
    if not notes:       
        index = 1
    else:
        max_key = max(notes.data.keys(), key=int)
        index = int(max_key) + 1

    # note = Note(input('Enter note:\n'))
    # tags = input('Enter Tags#:\n')
    # tags = [Tag(tag) for tag in tags.split(' ')]
    
    date = Date()
    record = Note_Record(index, note_str, date, tags)
    notes.add_record(record)
    # notes.serialize(FILE_PATH)
    return f'{index}. {record}'
    
        
def show_notes(*args):
    if not notes:
        return 'No notes in notebook'
    else:
        iterator = Iterator(notes)
        i = 0
        for record in iterator:
            print(record)
            i += 1
            if i%4 == 0:
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
        while True:
            category = input('Press "1" to edit notes, "2" - to edit Tags#: ')
            if category == '1' or category == '2':
                break
            print('Wrong choice')
        if category == '1':
            note = Note(input(f'Current record({record.note}): '))
        elif category == '2':
            tags = input(f'Current #Tags({record.tags}): ')
            tags = [Tag(tag) for tag in tags.split(' ')]
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


def clear_notes(*args):
    if notes:
        while True:
            choice = input('Press "y" to clear all records or "n" to discard: ')
            if choice in ['y', 'n']:
                break
            print('Wrong choice')
        if choice == 'y':
            notes.data.clear()
            return f'Notes was cleared {notes.data}'
        elif choice == 'n': 
            return f'{notes.data}'


def sort_notes(*args):
    while True:
        category = input('Press "1" to sort by date, "2" - to sort by index, "3" - to sort by #Tags: ')
        if category in ['1', '2', '3']:
            break
        print('Wrong choice')
    result = notes.sort(category)
    if not result:
        return 'No notes in notebook'
    else:
        i = 0
        for record in result:
            print(f'{record}\n')
            i += 1
            if i%4 == 0:
                try:
                    input("Press 'Enter' to continue\n")
                except KeyboardInterrupt:
                    break
    return "End\n"
  

def search_notes():
    while True:
        category = input('Press "1" to search in notes, "2" - in #Tags: ')
        if category == '1' or category == '2':
            break
        print('Wrong choice')
    search_str = input('Please enter string to search: ')
    if category == "1":
        search_results = notes.search(search_str, 1)
    elif category == "2":
        search_results = notes.search(search_str, 2)
    if search_results:
        return search_results
    else:
        print("No notes or Tags were found")


dict_command = {'add notes': add_note,
               'show notes': show_notes,
               'change notes': change_note,
               'delete notes': delete_note,
               'sort notes': sort_notes,
               'search notes': search_notes,
               'clear notes': clear_notes}
                
list_end = ['good bye', 'close', 'exit']


def parse_input(command_line: str) -> tuple[object, list]:
    line: str = command_line.lower().lstrip()
    match = re.search(r'^(\w+\s+\w{5})\s*(.*)', line,)
    user_command, args = match.group(1), match.group(2).split()
    if user_command in dict_command.keys():
        return dict_command[user_command], args
    else:
        return 'Wrong command'


def main_notes():
    # try:
    #     notes.deserialize(FILE_PATH)
    # except FileNotFoundError:
    #     print("No file found. New notebook was created.")
    
    
    while True:
        user_input = input('>>>')
        user_input = user_input.lower()
        
        if user_input in list_end:
            print('Good bye!')
            break
        command, args = parse_input(user_input)
        try:
            result = command(args)
            print(result)
        except KeyError:
            print('Wrong command')
       
        
if __name__ == '__main__':
    main_notes()
    