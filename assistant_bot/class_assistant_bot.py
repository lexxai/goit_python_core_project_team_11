from .class_commands import Commands
from .class_address_book import AddressBook

# from .class_notes import Notes
from .class_notes_ext import Notes_Storage
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import pickle
from pathlib import Path
from rich.console import Console
import types
from .class_command_completer import CommandCompleter


class Assistant_bot(Commands):
    def __init__(
        self,
        id: str = None,
        auto_backup: bool = True,
        auto_restore: bool = True,
        default_filename: str = "assistant_bot",
    ):
        self.id: str = id
        self.auto_backup: bool = auto_backup
        self.auto_restore: bool = auto_restore
        self.a_book: AddressBook = AddressBook(id=id)
        self.notes_storage: Notes_Storage = Notes_Storage()
        self.default_filename: str = default_filename
        self.restore_data()
        self._console = Console(no_color=False, force_terminal=True)

        # super().__init__(child = self)

    # def _callback(self, method_str: str, *args, **kwargs):
    #     #print(f"{__name__} [_callback] {method_str=}")
    #     method = self.__getattribute__(method_str)
    #     if method:
    #         return method(*args, **kwargs)

    def _gen_filename(self, filename: str) -> str:
        if self.id:
            filename = f"{self.id}_{filename}"
        return filename

    def backup_data(self, version: str = None, backup: bool = None) -> bool:
        if self.auto_backup or backup:
            if version:
                filename = f"{self.default_filename}_{version}.bin"
            else:
                filename = f"{self.default_filename}.bin"
            with open(self._gen_filename(filename), "wb") as file:
                pickle.dump(self, file)
            return True

    def restore_data(self, version: str = None, restore: bool = None) -> bool:
        if self.auto_restore or restore:
            if version:
                filename = f"{self.default_filename}_{version}.bin"
            else:
                filename = f"{self.default_filename}.bin"
            try:
                # print(f"{filename=}")
                with open(self._gen_filename(filename), "rb") as file:
                    content = pickle.load(file)
                    if type(content) == type(self):
                        self.__dict__.update(content.__dict__)
                        return True
            except Exception:
                return False

    def list_versions(self):
        filename = f"{self.default_filename}_*.bin"
        list_files = Path(".").glob(self._gen_filename(filename))
        result_version = []
        for found_file in list_files:
            result_version.append("version: {}".format(found_file.stem.split("_")[-1]))
        return "\n".join(result_version) if any(result_version) else True

    def main(self):
        history = PromptSession()
        while True:
            category = (
                input('Use interactive help "y" or "n" (default "y"): ').lower() or "y"
            )
            if category in ["y", "n"]:
                break
        while True:
            try:
                if category == "y":
                    user_input = history.prompt(
                        "\nEnter your command >>> ",
                        completer=CommandCompleter(parent=self),
                        auto_suggest=AutoSuggestFromHistory(),
                    )
                elif category == "n":
                    user_input = self._console.input(
                        "\n[bold]Enter your command >>> [/bold]"
                    )
            except KeyboardInterrupt:
                self._console.print("\r")
                break

            command, args, command_str = self.parse_input(user_input)
            try:
                if len(args) == 1 and args[0] == "?":
                    result = self.handler_help(command)
                else:
                    result = command(self, *args)

                if result:
                    if isinstance(result, types.GeneratorType):
                        for r in result:
                            self._console.print(r)
                    else:
                        self._console.print(result)

                if command == Commands.handler_exit:
                    break
            except Exception as e:
                self._console.print(f"COMMANDS ERROR:'{e}'")
        self.backup_data()

    # skip save state for rich.consol object
    def __getstate__(self):
        state = self.__dict__.copy()
        # Remove the unpicklable entries.
        del state["_console"]
        return state
