from .class_fields import Field, Name, Phone, Email, Address, Birthday
from datetime import date

class Record:

    def __init__(self, name: Name = None,
                 phone: Phone = None,
                 email: Email = None, 
                 address: Address = None, 
                 birthday: Birthday = None) -> None:
        self.name: Name = name
        self.email: Email = email
        self.address: Address = address
        self.phone: list(Phone) = []
        self.add_phone(phone)
        self.birthday: Birthday = birthday


    def add(self, field: Field) -> bool:
        result = None
        if isinstance(field, Phone):
            result = self.add_phone(field)
        elif isinstance(field, Birthday):
            result = self.add_birthday(field)
        elif isinstance(field, Email):
            result = self.add_email(field)
        elif isinstance(field, Address):
            result = self.add_address(field)
        return result
            

    def add_phone(self, phone: Phone) -> None:
        if (phone):
            if (isinstance(phone, list)):
                for ph in phone:
                    if ph not in self.phone:
                        self.phone.append(ph)
                return True
            elif phone not in self.phone:
                self.phone.append(phone)
                return True


    def change_phone(self, old_phone: Phone, new_phone: Phone) -> None:
        if old_phone and new_phone:
            for i, v in enumerate(self.phone):
                if self.phone[i] == old_phone:
                    self.phone[i] = new_phone
                    return True
    

    def remove_phone(self, phone: Phone) -> None:
        if phone in self.phone:
            self.phone.remove(phone)
            return True


    def get_phones(self) -> str:
        return ";".join([str(ph) for ph in self.phone])

    def filed_to_csv(self, value:str) -> str:
        """
            https://en.wikipedia.org/wiki/Comma-separated_values
        """
        value = str(value) if value else ""

        isolated_chars = (",",) 
        for ch in isolated_chars:
            if ch in value:
                return f'"{value}"'
        return value
    


    def get_csv_row(self) -> str:
        data = self.export_data()
        #data["phone"] = self.get_phones()
        row = ""
        for k, v in data.items():
            value = self.filed_to_csv(v)
            if len(row):
                row += "," + value
            else:
                row = value
        return row


    @staticmethod
    def get_data_header() -> str:
        cols = Record.get_data_header_list()
        return ",".join(cols)
    
    @staticmethod
    def get_data_header_list() -> tuple:
        cols = ("name", "phone", "email", "address", "birthday")
        return cols
    
    
    def import_data(self, data_row: dict):
        if data_row.get("name"):
            self.name = Name(data_row.get("name"))
            if data_row.get("phone"):
                phone = [ Phone(p) for p in data_row.get("phone").split(";")]
                self.add_phone(phone)
            if data_row.get("email"):
                self.add_email(Email(data_row.get("email")))
            if data_row.get("address"):
                self.add_address(Address(data_row.get("address")))
            if data_row.get("birthday"):
                self.add_birthday(Birthday(data_row.get("birthday")))
            return True
            

    def export_data(self) -> dict:
        result = {}
        for field in Record.get_data_header_list():
            result[field] = self.__dict__[field]
        if type(result.get("phone")) == list:
            result["phone"] = self.get_phones()
        return result


    def add_birthday(self, birthday: Birthday) -> None:
        self.birthday = birthday
        return True


    def delete_birthday(self) -> None:
        if self.birthday:
            self.birthday = None
            return True


    def add_email(self, email: Email) -> None:
        self.email = email
        return True


    def delete_email(self) -> None:
        if self.email:
            self.email = None
            return True

    
    def add_address(self, address: Address) -> None:
        self.address = address
        return True


    def delete_address(self) -> None:
        if self.address:
            self.address = None
            return True


    def days_to_birthday(self) -> int:
        result = None
        if self.birthday:
            date_now = date.today()
            date_now_year = date_now.year
            bd = self.birthday.value.replace(year=date_now_year)
            if bd < date_now:
                date_now_year += 1
            bd = self.birthday.value.replace(year=date_now_year)
            diff_bd = bd - date_now
            result = diff_bd.days
        return result

    def search_name_phone(self, pattern:str) -> bool:
            if self.name.search(pattern):
                return True
            for p in self.phone:
                if p.search(pattern):
                    return True
            return False


    def __repr__(self):
        return str(self)
        

    def __str__(self) -> str:
        cols = [f"name: {self.name}"]
        if len(self.phone):
            cols.append(f"phones: {self.get_phones()}")
        if self.email:
            cols.append(f"email: {self.email}")
        if self.address:
            cols.append(f"address: {self.address}")
        if self.birthday:
            cols.append(f"birthday: {self.birthday}")
        return ", ".join(cols)
