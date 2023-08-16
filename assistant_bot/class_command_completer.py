from prompt_toolkit.completion import Completion, Completer
from .class_commands import Commands
import re


class CommandCompleter(Completer, Commands):
    def clear_rich(self, test_str: str) -> str:
        regex = r"\[/?\w+\]"
        return re.sub(regex, "", test_str, 0, re.MULTILINE)

    def __init__(self, parent: object = None):
        # self.parent = parent
        # generate COMMANDS_AUTOCOMPLETE
        self.COMMANDS_AUTOCOMPLETE = {}
        for handler, commands in Commands.COMMANDS.items():
            command = commands[0]
            command_help = Commands.COMMANDS_HELP.get(handler, ("undefined"))[0]
            command_help = self.clear_rich(command_help)
            # prepare data for help variables
            if parent and "{" in command_help:
                command_help = command_help.format(
                    per_page=parent.a_book.max_records_per_page,
                    id_session=parent.a_book.id,
                )
            self.COMMANDS_AUTOCOMPLETE[command] = command_help
        # super().__init__()

    def get_completions(self, document, complete_event):
        # word = document.get_word_before_cursor()
        word = document.current_line
        # print(word)
        for command in self.COMMANDS_AUTOCOMPLETE.keys():
            if command.startswith(word):
                display = command
                yield Completion(
                    command,
                    start_position=-len(word),
                    display=display,
                    display_meta=self.COMMANDS_AUTOCOMPLETE.get(command),
                )
