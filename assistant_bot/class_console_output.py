from abc import ABC
from rich.console import Console, Style, Text
import types
from enum import Enum, auto


class Terminals(Enum):
    TERMINAL = auto()
    TERMINAL_RICH = auto()
    TELEGRAM = auto()
    VIBER = auto()


class ConsoleOutputAbstract(ABC):
    service: Enum

    def output(self, text: str, *args) -> str:
        ...


class TerminalClearRichOutputConsole:
    # def __init__(self):
    #     self._console = Console(
    #         no_color=True, force_terminal=True, style=Style(bold=False)
    #     )

    def get_clear_text(self, text: str) -> str:
        r_text = Text.from_markup(text)
        for segment in r_text:
            if segment.style:
                segment.style.bold = False
        text = r_text.plain
        return text


class TerminalOutput(ConsoleOutputAbstract, TerminalClearRichOutputConsole):
    service = Terminals.TERMINAL

    def output(self, text: str, *args) -> None:
        text = self.get_clear_text(text)
        print(f"Send to TerminalOutput: {text}")


class TerminalRichOutput(ConsoleOutputAbstract):
    service = Terminals.TERMINAL_RICH

    def __init__(self, *console_args, **console_kwargs):
        self._console = Console(*console_args, **console_kwargs)

    def output(self, text: str, *args) -> None:
        print("Send to TerminalRichOutput \n")
        if text:
            if isinstance(text, types.GeneratorType):
                for r in text:
                    self._console.print(r)
            else:
                self._console.print(text)


class Telegram:
    def __init__(self, token):
        self.token = token

    def send_message(self, text):
        print(f"Send {text} to Telegram")


class TelegramOutput(ConsoleOutputAbstract, TerminalClearRichOutputConsole):
    service = Terminals.TELEGRAM

    def __init__(self, token) -> None:
        self.telegram_client = Telegram(token)
        super().__init__()

    def output(self, text: str, *args) -> None:
        text = self.get_clear_text(text)
        self.telegram_client.send_message(text)


class Viber:
    def __init__(self, token):
        self.token = token

    def send_message(self, text):
        print(f"Send {text} to Viber")


class ViberOutput(ConsoleOutputAbstract, TerminalClearRichOutputConsole):
    service = Terminals.VIBER

    def __init__(self, token) -> None:
        self.viber_client = Viber(token)
        super().__init__()

    def output(self, text: str, *args) -> None:
        text = self.get_clear_text(text)
        self.viber_client.send_message(text)
