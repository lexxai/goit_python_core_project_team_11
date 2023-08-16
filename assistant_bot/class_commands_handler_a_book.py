from .class_commands_handler import Commands_Handler
from functools import wraps
from .class_fields import Name, Phone, Birthday, Email, Address
from .class_record import Record
from .class_address_book import AddressBook


class Commands_Handler_Address_Book(Commands_Handler):
    # for declare only, instance created on class Assistant_bot
    a_book: AddressBook

    def backup_data_address_book(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            if self.a_book and self.a_book.backup_data:
                self.a_book.backup_data()
            self.backup_data()
            # if self._callback is not None:
            #     self._callback("backup_data")
            return result

        return wrapper

    @Commands_Handler.output_operation_describe
    @backup_data_address_book
    @Commands_Handler.input_error
    def handler_add_address_book(self, *args) -> str:
        result = None
        user = args[0]
        args[1]
        phone = [Phone(p) for p in args[1:]]
        if user in self.a_book:
            result = self.a_book.get_record(user).add_phone(phone)
        else:
            rec = Record(Name(user), phone)
            result = self.a_book.add_record(rec)
        return result

    @Commands_Handler.output_operation_describe
    @backup_data_address_book
    @Commands_Handler.input_error
    def handler_change_phone(self, *args) -> str:
        user = args[0]
        old_phone = args[1]
        new_phone = args[2]
        return self.a_book.get_record(user).change_phone(
            Phone(old_phone), Phone(new_phone)
        )

    @Commands_Handler.output_operation_describe
    @Commands_Handler.input_error
    def handler_show_phone(self, *args) -> str:
        user = args[0]
        return self.a_book.get_record(user).get_phones()

    @Commands_Handler.output_operation_describe
    @backup_data_address_book
    @Commands_Handler.input_error
    def handler_delete_phone(self, *args) -> str:
        user = args[0]
        phone = args[1]
        return self.a_book.get_record(user).remove_phone(Phone(phone))

    @Commands_Handler.output_operation_describe
    @backup_data_address_book
    @Commands_Handler.input_error
    def handler_delete_record(self, *args) -> str:
        user = args[0]
        return self.a_book.remove_record(user)

    @Commands_Handler.output_operation_describe
    @backup_data_address_book
    @Commands_Handler.input_error
    def handler_delete_all_records(self, *args) -> str:
        if args[0] == "YES":
            return self.a_book.clear()

    @Commands_Handler.output_operation_describe
    def handler_show_address_book(self, *args) -> str:
        if self.a_book.len():
            return str(self.a_book)
        else:
            return "No users found, maybe you want to add them first?"

    @Commands_Handler.input_error
    def handler_show_page(self, *args) -> str:
        if len(args) and args[0]:
            self.a_book.max_records_per_page = int(args[0])
        try:
            page = next(self.a_book)
            return "\n".join([str(i) for i in page])
        except StopIteration:
            return "End list"

    def handler_show_csv(self, *args) -> str:
        if any(self.a_book.keys()):
            return self.a_book.get_csv()
        else:
            return "No users found, maybe you want to add them first?"

    @Commands_Handler.output_operation_describe
    @Commands_Handler.input_error
    def handler_export_csv(self, *args) -> str:
        if len(args):
            filename = args[0]
        else:
            filename = None
        return self.a_book.export_csv(filename)

    @Commands_Handler.output_operation_describe
    @Commands_Handler.input_error
    def handler_import_csv(self, *args) -> str:
        if len(args):
            filename = args[0]
        else:
            filename = None
        return self.a_book.import_csv(filename)

    @Commands_Handler.output_operation_describe
    @backup_data_address_book
    @Commands_Handler.input_error
    def handler_add_birthday(self, *args) -> str:
        user = args[0]
        birthday = args[1]
        return self.a_book.get_record(user).add(Birthday(birthday))

    @Commands_Handler.output_operation_describe
    @backup_data_address_book
    @Commands_Handler.input_error
    def handler_add_email(self, *args) -> str:
        user = args[0]
        email = args[1]
        return self.a_book.get_record(user).add(Email(email))

    @Commands_Handler.output_operation_describe
    @backup_data_address_book
    @Commands_Handler.input_error
    def handler_add_address(self, *args) -> str:
        user = args[0]
        address = " ".join(args[1:])
        return self.a_book.get_record(user).add(Address(address))

    @Commands_Handler.output_operation_describe
    @backup_data_address_book
    @Commands_Handler.input_error
    def handler_delete_birthday(self, *args) -> str:
        user = args[0]
        return self.a_book.get_record(user).delete_birthday()

    @Commands_Handler.output_operation_describe
    @backup_data_address_book
    @Commands_Handler.input_error
    def handler_delete_email(self, *args) -> str:
        user = args[0]
        return self.a_book.get_record(user).delete_email()

    @Commands_Handler.output_operation_describe
    @backup_data_address_book
    @Commands_Handler.input_error
    def handler_delete_address(self, *args) -> str:
        user = args[0]
        return self.a_book.get_record(user).delete_address()

    @Commands_Handler.output_operation_describe
    @Commands_Handler.input_error
    def handler_days_to_birthday(self, *args) -> str:
        user = args[0]
        result = self.a_book.get_record(user).days_to_birthday()
        if result is None:
            result = f"No birthday is defined for user: {user} "
        elif result == 0:
            result = f"{result} days, Today is user {user}'s birthday !!!"
        else:
            result = f"{result} days"
        return result

    @Commands_Handler.output_operation_describe
    @Commands_Handler.input_error
    def handler_congrats_in_days(self, *args) -> str:
        days = int(args[0])
        result = self.a_book.congrats_in_days(days)
        return result

    @Commands_Handler.output_operation_describe
    @Commands_Handler.input_error
    def handler_show_birthday(self, *args) -> str:
        user = args[0]
        result = str(self.a_book.get_record(user).birthday)
        return result

    @Commands_Handler.output_operation_describe
    @Commands_Handler.input_error
    def handler_show_email(self, *args) -> str:
        user = args[0]
        result = str(self.a_book.get_record(user).email)
        return result

    @Commands_Handler.output_operation_describe
    @Commands_Handler.input_error
    def handler_show_address(self, *args) -> str:
        user = args[0]
        result = str(self.a_book.get_record(user).address)
        return result

    @Commands_Handler.output_operation_describe
    @Commands_Handler.input_error
    def handler_search_address_book(self, *args) -> str:
        pattern = args[0]
        result = self.a_book.search(pattern)
        return result

    @Commands_Handler.output_operation_describe
    def handler_list_csv(self, *args) -> str:
        result = self.a_book.list_csv()
        return result
