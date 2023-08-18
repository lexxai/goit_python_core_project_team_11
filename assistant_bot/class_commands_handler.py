from functools import wraps
from rich.console import Console


class Commands_Handler:
    _console: Console

    # decorator
    def output_operation_describe(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            if type(result) == str:
                return result
            else:
                return (
                    "[green]Done[green]"
                    if result
                    else "[yellow]The operation " "was not successful[/yellow]"
                )

        return wrapper

    # decorator
    def input_error(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except (KeyError, ValueError, IndexError) as e:
                error = str(e)
                return (
                    "[red]Sorry, there are not enough parameters "
                    f"or their value may be incorrect {error}. "
                    "Please use the help for more information. [/red]"
                )
            except FileNotFoundError:
                return "[red]Sorry, there operation with file is incorrect.[/red]"
            except Exception as e:
                return f"[red]**** Exception other: {e} [/red]"

        return wrapper

    # interface
    def backup_data():
        ...
