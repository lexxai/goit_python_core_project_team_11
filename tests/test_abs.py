from abc import ABC, abstractmethod


class BaseConsoleABS(ABC):
    @abstractmethod
    def send_text(self, text: str):
        ...


class Console(BaseConsoleABS):
    def send_text(self, text: str):
        print(f"CONSOLE: {text}")


class Telegram(BaseConsoleABS):
    def send_text(self, text: str):
        print(f"TELEGRAM: {text}")


class Bott:
    def __init__(self, console: BaseConsoleABS):
        self.console = console

    def main(self):
        self.console.send_text("HELLO WORLD, I'M is Boot")


my_console1 = Telegram()
my_boot1 = Bott(console=my_console1)
my_boot1.main()


my_console2 = Console()
my_boot2 = Bott(console=my_console2)
my_boot2.main()
