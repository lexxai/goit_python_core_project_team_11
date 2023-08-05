from .class_fields import Note, Tag
#from datetime import date


class Note_Record:

    def __init__(self, note: Note = None,
                 tags: list[Tag] = None) -> None:
        self.note: Note = note
        self.tags: list[Tag] = tags


    def add_note(self, note: Note, tags: list[Tag] = []) -> None:
        self.note: Note = note
        self.tags: list[Tag] = tags


    def add_tags(self, note: Note, tags: list[Tag]) -> None:
        self.tags: list[Tag] = tags


    def get_tags(self) -> str:
        return " #".join([str(tag) for tag in self.tags])


    def __str__(self) -> str:
        cols = [f"note: {self.note}"]

        if len(self.tags):
            cols.append(f"tags: {self.get_tags()}")

        return ", ".join(cols)
