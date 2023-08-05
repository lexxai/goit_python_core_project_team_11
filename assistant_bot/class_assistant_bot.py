from .class_commands import Commands
from .class_address_book import AddressBook
from .class_notes import Notes
import pickle



class Assistant_bot(Commands):

    def __init__(self, 
                 id: str = None,
                 auto_backup: bool = True,
                 auto_restore: bool = True):

        self.id: str = id
        self.auto_backup = auto_backup
        self.auto_restore = auto_restore
        self.a_book: AddressBook = AddressBook(id=id)
        self.a_notes: Notes = Notes(id=id)
        self.default_filename: str = "assistant_bot"

        self.restore_data()     
        
        super().__init__(a_book=self.a_book, 
                         a_notes=self.a_notes, 
                         backup_callback=self.backup_data,
                         restore_callback=self.restore_data,
                         )


    def _gen_filename(self, filename: str) -> str:
        if self.id:
            filename = f"{self.id}_{filename}"
        return filename      


    def backup_data(self, version:str = None, backup:bool = None) -> bool:
        if self.auto_backup or backup:
            if version:
                filename = f"{self.default_filename}_{version}.bin"
            else:
                filename = f"{self.default_filename}.bin"
            with open(self._gen_filename(filename), "wb") as file:
                pickle.dump(self, file)
            return True


    def restore_data(self, version:str = None, restore:bool = None) -> bool:
        if self.auto_restore or restore:
            if version:
                filename = f"{self.default_filename}_{version}.bin"
            else:
                filename = f"{self.default_filename}.bin"
            try:    
                with open(self._gen_filename(filename), "rb") as file:
                    content = pickle.load(file)
                    if type(content) == type(self):
                        self.__dict__.update(content.__dict__)
                        return True
            except Exception:
                return False


    def main(self):
        
        while True:
            try:
                user_input = input("Enter your command >>> ")
            except KeyboardInterrupt:
                print("\r")
                break

            command, args = self.parse_input(user_input)

            if len(args) == 1 and args[0] == "?":
                result = self.handler_help(command)
            else:
                result = command(self,*args)

            if result:
                print(result)

            if command == Commands.handler_exit:
                break

        self.backup_data()
