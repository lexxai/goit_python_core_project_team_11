from .DataNotesTags import AddressNotes, RecordNotes

class WorkNotesTags:
    def __init__(self):
        self.dict_notes = AddressNotes()
        self.notes = {}
        self.tags = {}
        self.list_end = ['good bye', 'close', 'exit']
    
    def no_command(*args):
        return 'unknown_command'

    def add_notes(self, note_tags_str):
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
        id: str = self.dict_notes.get_next()
        self.tags[str(id)] = tags_list 
        self.notes[str(id)] = note
        rec: RecordNotes = self.dict_notes.get(str(id))
        if rec:
            return rec.add_tag(tags_list)
        rec = RecordNotes(id, dict_notes_tags)
        return self.dict_notes.add_record(rec)

    def change_note_tag(self, text):
        search = '#'
        note_new = ''
        tag_new = []
        tag_old = []
        new_note_tags = {}
        text_split = text.split()
        key: str = text_split[0]
        text_split.remove(key)
        id: str = self.dict_notes.get_next()
        id -= 1
        if key == str(id):
            for i in text_split:
                if search not in i:
                    note_new += i + ' '.strip()
            for i in text_split:
                if i.startswith('#'):
                    tag_new.append(i)
            if tag_new:
                for k,v in self.tags.items():
                    if key == k:
                        for t in v:
                            tag_new.append(t)
                del self.tags[key]
                self.tags[str(key)] = tag_new
            else:
                for k,v in self.tags.items():
                    if key == k:
                        for t in v:
                            tag_old.append(t)
            note_old = self.notes.get(str(key))
            note_old.strip()
            if note_new != '':
                if tag_new:
                    new_note_tags[note_new] = tag_new
                else:
                    new_note_tags[note_new] = tag_old
            else:
                if tag_new:
                    new_note_tags[note_old] = tag_new
                else:
                    new_note_tags[note_old] = tag_old
            rec: RecordNotes = self.dict_notes.get(str(key))
            if rec:
                id = key
                rec = RecordNotes(id, new_note_tags)
                return self.dict_notes.add_record(rec)
        return 'Notes with this number do not exist'

    def show_notes(self, note_tags_str):
        return self.dict_notes

    '''def parser_notes(self, text: str):
        note_tags = text.split()
        command = ''
        note_tags_str: str = ''
        command = command + note_tags[0] + ' '
        note_tags.pop(0)
        command = command + note_tags[0]
        note_tags.pop(0)
        for i in note_tags:
            note_tags_str += i + ' '
        if command in self.dict_command.keys():
            return self.dict_command.get(command), note_tags_str
        return self.no_command, text

    def main(self):
        while True:
            user_input = input('>>>')
            user_input = user_input.lower()
            
            if user_input in self.list_end:
                print('Good bye!')
                break
            command, note_tags_str= self.parser_notes(user_input)
            result = command(note_tags_str)
            print(result)'''