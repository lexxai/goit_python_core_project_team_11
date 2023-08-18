from abc import ABC
from rich.console import Console
import types
from enum import Enum, auto


class Terminals(Enum):
    TERMINAL = auto()
    TERMINAL_RICH = auto()
    TELEGRAM = auto()
    VIBER = auto()


class ConsoleOutputAbstract(ABC):
    service: Enum

    def output(self, text: str, *args) -> None:
        ...


class TerminalOutput(ConsoleOutputAbstract):
    service = Terminals.TERMINAL

    def output(self, text: str, *args) -> None:
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


class TelegramOutput(ConsoleOutputAbstract):
    service = Terminals.TELEGRAM

    def __init__(self, token) -> None:
        self.telegram_client = Telegram(token)

    def output(self, text: str, *args) -> None:
        self.telegram_client.send_message(text)


class Viber:
    def __init__(self, token):
        self.token = token

    def send_message(self, text):
        print(f"Send {text} to Viber")


class ViberOutput(ConsoleOutputAbstract):
    service = Terminals.VIBER

    def __init__(self, token) -> None:
        self.viber_client = Viber(token)

    def output(self, text: str, *args) -> None:
        self.viber_client.send_message(text)
