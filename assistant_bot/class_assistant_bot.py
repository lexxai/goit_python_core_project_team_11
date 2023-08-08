from .class_commands import Commands
from .class_address_book import AddressBook
from .class_notes_ext import Notes
import pickle
from  pathlib import Path



class Assistant_bot(Commands):

    def __init__(self, 
                 id: str = None,
                 auto_backup: bool = True,
                 auto_restore: bool = True,
                 default_filename: str = "assistant_bot"
                 ):

        self.id: str = id
        self.auto_backup: bool = auto_backup
        self.auto_restore: bool = auto_restore
        self.a_book: AddressBook = AddressBook(id=id)
        self.a_notes: Notes = Notes(id=id)
        self.default_filename: str = default_filename

        self.restore_data()     

        #super().__init__(child = self)

    def _callback(self, method_str: str, *args, **kwargs):
        #print(f"{__name__} [_callback] {method_str=}")
        method = self.__getattribute__(method_str)
        if method:
            return method(*args, **kwargs)


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

    def list_versions(self):
        filename = f"{self.default_filename}_*.bin"
        list_files = Path('.').glob(self._gen_filename(filename))
        result_version = []
        for found_file in list_files:
            result_version.append("version: {}".format(found_file.stem.split("_")[-1]))
        return "\n".join(result_version) if any(result_version) else True

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
