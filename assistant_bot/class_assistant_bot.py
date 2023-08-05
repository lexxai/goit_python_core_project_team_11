from .class_commands import Commands
from .class_address_book import AddressBook
from .class_notes import Notes



class Assistant_bot(Commands):

    def __init__(self, 
                 id: str = None,
                 auto_backup: bool = True,
                 auto_restore: bool = True):
        self.id_session: str = id
        self.a_book: AddressBook = AddressBook(id=id,
                                  auto_backup = auto_backup,
                                  auto_restore = auto_restore)
        self.a_notes: Notes = Notes(id=id,
                                  auto_backup=auto_backup,
                                  auto_restore=auto_restore)
        
        super().__init__(self.a_book, self.a_notes)


    def main(self):
        
        if self.a_book.auto_restore:
            self.a_book.restore_data()

        if self.a_notes.auto_restore:
            self.a_notes.restore_data()

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

        if self.a_book.auto_backup:
            self.a_book.backup_data()

        if self.a_notes.auto_backup:
            self.a_notes.backup_data()
