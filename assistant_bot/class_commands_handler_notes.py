from .class_commands_handler import Commands_Handler
from .class_notes_ext import Notes_Storage
from functools import wraps


class Commands_Handler_Notes(Commands_Handler):
    # for declare only, instance created on class Assistant_bot
    notes_storage: Notes_Storage

    def backup_data_note(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            # class_assistant_bot.py - backup_data
            self.backup_data()
            return result

        return wrapper

    @backup_data_note
    @Commands_Handler.input_error
    def handler_add_note(self, *args) -> str:
        return self.notes_storage.add_note(*args)

    @backup_data_note
    @Commands_Handler.input_error
    def handler_change_notes(self, *args):
        return self.notes_storage.change_note(*args)

    @backup_data_note
    @Commands_Handler.input_error
    def handler_delete_notes(self, *args):
        return self.notes_storage.delete_note(*args)

    @backup_data_note
    @Commands_Handler.input_error
    def handler_clear_notes(self, *args):
        return self.notes_storage.clear_notes(*args)

    @Commands_Handler.input_error
    def handler_search_notes(self, *args):
        return self.notes_storage.search_notes(*args)

    @Commands_Handler.input_error
    def handler_search_notes(self, *args):
        return self.notes_storage.search_notes(*args)

    @Commands_Handler.input_error
    def handler_sort_notes(self, *args):
        return self.notes_storage.sort_notes(*args)

    @Commands_Handler.input_error
    def handler_show_notes(self, *args) -> str:
        return self.notes_storage.show_notes()
