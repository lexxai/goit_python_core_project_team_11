from .class_commands_handler import Commands_Handler
from .class_commands_handler_notes import Commands_Handler_Notes
from .class_commands_handler_a_book import Commands_Handler_Address_Book
from .sorting import main as sorting

from rich.table import Table
import math

# from functools import wraps

import sys

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version


class Commands(Commands_Handler_Address_Book, Commands_Handler_Notes):
    def split_line_by_space(self, line: str) -> list[str]:
        """split_line_by_space with quotes

        Args:
            line (str): "Jon 12" +32323243434 33033440

        Returns:
            list: ["Jon 12", "+32323243434", "33033440"]
        """
        parts = []
        current_part = ""
        inside_quotes = False
        for char in line:
            if char == " " and not inside_quotes:
                parts.append(current_part.strip())
                current_part = ""
            elif char == '"':
                inside_quotes = not inside_quotes
            else:
                current_part += char
        parts.append(current_part.strip())
        return list(filter(lambda x: x, parts))

    def parse_input(self, command_line: str) -> tuple[object, list, str]:
        line: str = command_line.lower().lstrip()
        for command, commands in self.COMMANDS.items():
            for command_str in commands:
                if len(line) > len(command_str):
                    command_str += " "
                if line.startswith(command_str):
                    # args = command_line[len(command_str):].strip().split()
                    args = self.split_line_by_space(
                        command_line[len(command_str) :].strip()
                    )
                    return command, args, command_str
        return Commands.handler_undefined, [line], None

    @Commands_Handler.output_operation_describe
    @Commands_Handler.input_error
    def handler_sorting(self, *args) -> str:
        path = args[0]
        return sorting(path)

    def handler_hello(self, *args) -> str:
        return "How can I help you?"

    def get_list_commands(self, help_filter: str = None) -> str:
        commands = []
        for cs in Commands.COMMANDS.values():
            if help_filter and not any(
                filter(lambda x: str(x).find(help_filter) != -1, cs)
            ):
                continue
            c_str = ""
            c_alias = []
            for c in list(cs):
                if len(c_str) == 0:
                    c_str = c
                else:
                    c_alias.append(f"'{c}'")
            c_alias_str = ",".join(c_alias)
            if any(c_alias):
                c_str += f" ({c_alias_str})"
            commands.append(c_str)
        command_str = (
            "\n[i]The full command syntax is available on request: command ?"
            " [Example: +a ?][/i] \n[b]List of commands:[/b] \n"
            + ", ".join(sorted(commands))
        )  # noqa: E501
        return command_str

    def add_help_parameters(self, command_str: str) -> str:
        if command_str:
            if "{" in command_str:
                command_str = command_str.format(
                    per_page=self.a_book.max_records_per_page, id_session=self.a_book.id
                )
        return command_str

    def help_table_rich(self, rows_cat, column: int, columns: int = 4):
        len_t = math.ceil(len(rows_cat) / columns)
        min_t = (column) * len_t
        max_t = (column + 1) * len_t
        # print(f"{len_t=}, {min_t=}, {max_t=}")
        rows_category = rows_cat[min_t:max_t]
        if rows_category:
            table = Table(row_styles=["green", ""], expand=True)
            table.add_column("Command", no_wrap=True, max_width=12)
            table.add_column("Alias", no_wrap=True, max_width=6)
            # table.add_column("Category",no_wrap=True, min_width=10)
            # table.add_column("Help",no_wrap=True, max_width=40)

            prev_cat = rows_category[0][3]
            # generate table
            for row in rows_category:
                cat = row[3]
                if prev_cat != cat:
                    table.add_section()
                    prev_cat = cat
                table.add_row(*row[:2])
            return table

    def help_full_table_rich(self, rows_cat, column: int, columns: int = 2):
        len_t = math.ceil(len(rows_cat) / columns)
        min_t = (column) * len_t
        max_t = (column + 1) * len_t
        # print(f"{len_t=}, {min_t=}, {max_t=}")
        rows_category = rows_cat[min_t:max_t]
        if rows_category:
            table = Table(row_styles=["green", ""], expand=True)
            table.add_column("Command", no_wrap=True, max_width=12)
            table.add_column("Alias", no_wrap=True, max_width=4)
            # table.add_column("Category",no_wrap=True, min_width=10)
            table.add_column("Help", no_wrap=True, max_width=40)
            prev_cat = rows_category[0][3]
            # generate table
            for row in rows_category:
                cat = row[3]
                if prev_cat != cat:
                    table.add_section()
                    prev_cat = cat
                table.add_row(*row[:3])
            return table

    def get_list_commands_rich(self, help_filter: str = None, full: bool = True) -> str:
        # title="\nList of commands. The full command syntax "
        #        "is available on request: command ? [Example: +a ?]"
        rows = []
        for hand, cs in Commands.COMMANDS.items():
            # if help_filter and not any(
            #     filter(lambda x: str(x).find(help_filter) != -1, cs)):
            #     continue
            if help_filter and cs[0].find(help_filter) == -1:
                continue
            aliases = ",".join(cs[1:])
            command = cs[0]
            help_str = Commands.COMMANDS_HELP[hand][0][:100]
            help_str = self.add_help_parameters(help_str)
            category = Commands.COMMANDS_HELP[hand][1]
            row = [command, aliases, help_str, category]
            rows.append(row)
        # sorting
        rows_category = sorted(rows, key=lambda r: (r[3], r[0]))

        cols = 2 if full else 6
        table_main = Table.grid(expand=True)
        for _ in range(cols):
            table_main.add_column()

        cols_data = []
        for i in range(cols):
            if full:
                cols_data.append(self.help_full_table_rich(rows_category, i, cols))
            else:
                cols_data.append(self.help_table_rich(rows_category, i, cols))
        table_main.add_row(*cols_data),
        return table_main

    def handler_help_full(self, *args, help_filter=None) -> str:
        return self.handler_help(*args, help_filter=help_filter, full=True)

    def handler_help_table_title(self, table, title: str = None):
        yield title
        yield table

    def handler_help(self, *args, help_filter=None, full: bool = False) -> str:
        # print(f"{self._console.is_terminal=}")
        command = None
        if len(args):
            command = args[0]
        if not command:
            if self._console.is_terminal is False:
                # TERMINAL MODE OFF
                command_str = self.get_list_commands(help_filter)
            else:
                # TERMINAL MODE ON
                command_str = self.get_list_commands_rich(help_filter, full=full)
                title = (
                    "\nList of commands. The full command syntax "
                    "is available on request: command ? [Example: +a ?]"
                )
                command_str = self.handler_help_table_title(command_str, title)

        else:
            if type(command) == str:
                command = " ".join(args)
                command = self.get_command_handler(command)
            command_str: str = Commands.COMMANDS_HELP.get(command, (None, None))[
                0
            ]  # noqa: E501
            if command_str:
                if "{" in command_str:
                    command_str = command_str.format(
                        per_page=self.a_book.max_records_per_page,
                        id_session=self.a_book.id,
                    )
                command_str = f"[i]{command_str}[/i]"
            else:
                command_str: str = (
                    "[yellow]Help for this command is not yet available[/yellow]"
                )

        return command_str

    def handler_exit(self, *args) -> str:
        return "[i]Goodbye. We are looking forward to seeing you again.[/i]"

    def handler_undefined(self, *args) -> str:
        command = None
        if any(args):
            command = args[0]
        return self.handler_help(help_filter=command)

    def get_command_handler(self, command: str) -> object:
        for ch in Commands.COMMANDS:
            for cs in Commands.COMMANDS[ch]:
                if cs == command:
                    return ch
        return Commands.handler_undefined

    @Commands_Handler.output_operation_describe
    @Commands_Handler.input_error
    def handler_backup(self, *args) -> bool:
        version = None
        result = None
        if any(args):
            version = args[0]
        result = self.backup_data(version=version, backup=True)
        # if self._callback is not None:
        #     result = self._callback("backup_data",version = version, backup = True)
        return result

    @Commands_Handler.output_operation_describe
    @Commands_Handler.input_error
    def handler_restore(self, *args) -> bool:
        version = None
        result = None
        if any(args):
            version = args[0]
        result = self.restore_data(version=version, restore=True)
        # if self._callback is not None:
        #     result = self._callback("restore_data", version = version, restore = True)
        return result

    def handler_list_versions(self, *args) -> str:
        result = None
        result = self.list_versions()
        # if self._callback is not None:
        #     result = self._callback("list_versions")
        return result

    @Commands_Handler.output_operation_describe
    @Commands_Handler.input_error
    def handler_show_app_version(self, *args) -> str:
        try:
            version_str = version(__package__)
        except Exception:
            version_str = "undefined"
        return f"Version: '{ version_str }', package: {__package__}"

    @Commands_Handler.input_error
    def api(self, command: str, *args: list[str], verbose: bool = True) -> None:
        """API for run commands in batch mode

        Args:
            command (str): API command
            list[str]: API command arguments

        Returns:
            print API command result

        """
        result = self.get_command_handler(command)(self, *args)
        if verbose:
            self._console.print(
                f"[green]api command '{command}'[/green]: [yellow]{result}[/yellow]"
            )
        else:
            return result

    """
    CONSTANT DICT OF COMMANDS LIST 
    - key is pointer to handler function 
    - value is list of chat bot commands
    """
    COMMANDS = {
        handler_hello: ("hello",),
        Commands_Handler_Address_Book.handler_delete_record: ("delete user", "-"),
        Commands_Handler_Address_Book.handler_delete_all_records: (
            "delete all records",
            "---",
        ),
        Commands_Handler_Address_Book.handler_change_phone: ("change phone", "=p"),
        Commands_Handler_Address_Book.handler_delete_phone: ("delete phone", "-p"),
        Commands_Handler_Address_Book.handler_show_phone: ("show phone", "?p"),
        Commands_Handler_Address_Book.handler_show_page: ("show page", "?pg"),
        Commands_Handler_Address_Book.handler_show_csv: ("show csv", "?csv"),
        Commands_Handler_Address_Book.handler_export_csv: ("export csv", "e csv"),
        Commands_Handler_Address_Book.handler_import_csv: ("import csv", "i csv"),
        handler_help: ("help", "?"),
        handler_help_full: ("help full", "??"),
        Commands_Handler_Address_Book.handler_add_birthday: ("add birthday", "+b"),
        Commands_Handler_Address_Book.handler_delete_birthday: (
            "delete birthday",
            "-b",
        ),
        Commands_Handler_Address_Book.handler_add_email: ("add email", "+e"),
        Commands_Handler_Address_Book.handler_delete_email: ("delete email", "-e"),
        Commands_Handler_Address_Book.handler_add_address_book: (
            "add address book",
            "+ab",
        ),
        Commands_Handler_Address_Book.handler_add_address: ("add address", "+a"),
        Commands_Handler_Address_Book.handler_delete_address: ("delete address", "-a"),
        Commands_Handler_Address_Book.handler_days_to_birthday: ("to birthday", "2b"),
        Commands_Handler_Address_Book.handler_show_birthday: ("show birthday", "?b"),
        Commands_Handler_Address_Book.handler_show_email: ("show email", "?e"),
        Commands_Handler_Address_Book.handler_show_address_book: (
            "show address book",
            "?ab",
        ),
        Commands_Handler_Address_Book.handler_show_address: ("show address", "?a"),
        handler_backup: ("backup", "bak"),
        handler_restore: ("restore", "res"),
        handler_list_versions: ("show versions", "?v"),
        Commands_Handler_Address_Book.handler_list_csv: ("list csv", "l csv"),
        Commands_Handler_Address_Book.handler_congrats_in_days: (
            "next birthdays",
            "+nb",
        ),
        Commands_Handler_Address_Book.handler_search_address_book: (
            "search address book",
            "?ab=",
        ),
        handler_exit: ("quit", "exit", "q"),
        # notes
        Commands_Handler_Notes.handler_add_note: ("add note", "+n"),
        Commands_Handler_Notes.handler_show_notes: ("show notes", "?n"),
        Commands_Handler_Notes.handler_change_notes: ("change note", "=n"),
        Commands_Handler_Notes.handler_delete_notes: ("delete note", "-n"),
        Commands_Handler_Notes.handler_clear_notes: ("clear notes", "---n"),
        Commands_Handler_Notes.handler_search_notes: ("search notes", "?n="),
        Commands_Handler_Notes.handler_sort_notes: ("sort notes", "sn"),
        # sorting
        handler_sorting: ("sort folder", "sorting"),
        handler_show_app_version: ("app version", "version"),
    }

    COMMANDS_CATEGORY = ("SYS", "A_BOOK", "NOTES", "SYS_STORE")

    """
    CONSTANT DICT OF COMMANDS HELP 
    - key is pointer to handler function 
    - value is help text for commands
    """
    COMMANDS_HELP = {
        handler_hello: ("Just hello", "SYS"),
        Commands_Handler_Address_Book.handler_delete_record: (
            "Delete ALL records of user. Required [u]username[/u].",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_delete_all_records: (
            "Delete ALL records of ALL user." "Required parameter [u]YES[/u]",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_change_phone: (
            "Change user's phone. " "Required [u]username[/u], old phone, new phone",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_delete_phone: (
            "Delete user's phone. Required [u]username[/u], [u]phone[/u]",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_delete_email: (
            "Delete user's email. Required [u]username[/u], [u]email[/u]",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_delete_address: (
            "Delete user's address. " "Required [u]username[/u], [u]address[/u]",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_delete_birthday: (
            "Delete user's birthday. Required [u]username[/u]",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_add_birthday: (
            "Add or replace the user's birthday. "
            "Required [u]username[/u], [u]birthday[/u], "
            "[white]please use ISO 8601 or DD.MM.YYYY date format[/white]",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_add_email: (
            "Add or replace the user's email. "
            "Required [u]username[/u], [u]email[/u]",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_add_address: (
            "Add or replace the user's address. "
            "Required [u]username[/u], [u]address[/u]",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_show_phone: (
            "Show user's phones. Required [u]username[/u].",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_show_birthday: (
            "Show user's birthday. Required [u]username[/u].",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_show_email: (
            "Show user's email. Required [u]username[/u].",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_show_address: (
            "Show user's address. Required [u]username[/u].",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_show_address_book: (
            "Show all user records in the address book.",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_show_page: (
            "Show all user's record per page. "
            "Optional parameter size of page [{per_page}]",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_show_csv: (
            "Show all user's record in csv format",
            "A_BOOK_CSV",
        ),
        Commands_Handler_Address_Book.handler_export_csv: (
            "Export all user's record in csv format to file. "
            "Optional parameter filename",
            "A_BOOK_CSV",
        ),
        Commands_Handler_Address_Book.handler_import_csv: (
            "Import all user's record in csv format to file. "
            "Optional parameter filename",
            "A_BOOK_CSV",
        ),
        Commands_Handler_Address_Book.handler_days_to_birthday: (
            "Show days until the user's birthday. " "Required [u]username[/u].",
            "A_BOOK",
        ),
        Commands_Handler_Address_Book.handler_add_address_book: (
            "Add user's phone or "
            "multiple phones separated by space. "
            "Required [u]username[/u] and [u]phone[/u].",
            "A_BOOK",
        ),
        handler_help: (
            "Short List of commands. "
            "Also you can use '?' "
            "for any command as parameter.",
            "SYS",
        ),
        handler_help_full: (
            "Full List of commands and their description. "
            "Also you can use '?' "
            "for any command as parameter.",
            "SYS",
        ),  # noqa: E501
        handler_exit: ("Exit of bot.", "SYS"),
        Commands_Handler_Address_Book.handler_search_address_book: (
            "Search user by pattern in name or phone",
            "A_BOOK",
        ),
        handler_backup: (
            "Backup all records. Optional parameter is the version. "
            "P.S. it done automatically after any changes on records",
            "SYS_STORE",
        ),
        handler_restore: (
            "Restore all records. Optional parameter is the version.",
            "SYS_STORE",
        ),
        handler_list_versions: ("List of saved backup versions", "SYS_STORE"),
        Commands_Handler_Address_Book.handler_list_csv: (
            "List of saved cvs files",
            "A_BOOK_CSV",
        ),
        handler_undefined: (
            "[yellow]Help for this command is not yet available[/yellow]",
            "SYS",
        ),
        # notes
        Commands_Handler_Notes.handler_add_note: ("Add a new note record", "NOTES"),
        Commands_Handler_Notes.handler_show_notes: (
            "Show all user's records in Notes.",
            "NOTES",
        ),
        Commands_Handler_Notes.handler_change_notes: ("Change note by index.", "NOTES"),
        Commands_Handler_Notes.handler_delete_notes: ("Delete note by index", "NOTES"),
        Commands_Handler_Notes.handler_clear_notes: ("Clear all notes", "NOTES"),
        Commands_Handler_Notes.handler_search_notes: (
            "Search notes or tags by pattern. Optional parameters "
            "is A and B. A is '1' to search in notes, "
            "'2' - in #Tags. B is what to search.",
            "NOTES",
        ),
        Commands_Handler_Notes.handler_sort_notes: (
            "Sort notes by type that user choose. Optional parameter "
            " is '1' to sort by date, '2' - "
            "to sort by index, '3' - to sort by #Tags",
            "NOTES",
        ),
        handler_sorting: ("Sorting files of folder. Required path to folder.", "NOTES"),
        handler_show_app_version: (
            "Show version of application. ID: {id_session}",
            "SYS",
        ),
        Commands_Handler_Address_Book.handler_congrats_in_days: (
            "Show list of users with birthdays, which will "
            "be in certain days. Required days parameter",
            "A_BOOK",
        ),
    }
