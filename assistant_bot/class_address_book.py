from collections import UserDict
from .class_record import Record
import csv
import pickle
from  pathlib import Path
from datetime import datetime


class AddressBook(UserDict):

    def __init__(self, records_per_page :int = 10, 
                 default_filename :str = "addresbook",
                 id: str = None,
                 auto_backup: bool = False,
                 auto_restore: bool = False,
                 *args, **kwargs):
        self.max_records_per_page = records_per_page
        self.default_filename = default_filename
        self.auto_backup = auto_backup
        self.auto_restore = auto_restore
        self.id = id
        super().__init__(self, *args, **kwargs)
        

    def add_record(self, rec):
        key = rec.name.value
        self.data[key] = rec
        return True
        
    
    def get_record(self, key) -> Record:
        return self.data[key]


    def remove_record(self, key) -> None:
        del self.data[key]
        return True

    def search(self, pattern: str) -> str:
        result = []
        for r in self.data.values():
            if r.search_name_phone(pattern):
                result.append(str(r))
        return "\n".join(result)


    def clear(self) -> None:
        self.data.clear()
        return True


    def len(self):
        return len(self.data)


    def __repr__(self) -> str:
        return str(self)


    def get_csv(self) -> str:
        result = [Record.get_data_header()]
        result.extend([ str(r.get_csv_row()) for r in self.data.values() ])
        return "\n".join(result)

    
    def export_data(self) -> list:
        return [r.export_data() for r in self.data.values()]

     
    def _gen_filename(self, filename: str) -> str:
        if self.id:
            filename = f"{self.id}_{filename}"
        return filename


    def _clean_filename(self, filename: str) -> str:
        if self.id and self.id in filename:
            filename = filename[len(self.id)+1:]
        return filename


    def export_csv(self, *args) -> str:
        if len(args) and args[0]:
            filename = args[0]
        else:
            filename = self.default_filename + ".csv"
        if filename and any(self.keys()):
            try:
                with open(self._gen_filename(filename), "w", newline='') as csv_file:
                    fieldnames = Record.get_data_header_list()
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    rows = self.export_data()
                    if len(rows):
                        csv_writer.writeheader()
                        csv_writer.writerows(rows)
                return f'Exported successfully to "{filename}" file'
            except Exception:
                return False
        else:
            return False


    def import_csv(self, *args) -> str:
        if len(args) and args[0]:
            filename = args[0]
        else:
            filename = self.default_filename + ".csv"
        result = False
        if filename:
            try:
                with open(self._gen_filename(filename), "r") as csv_file:
                    fieldnames = Record.get_data_header_list()
                    csv_reader = csv.DictReader(
                        csv_file, fieldnames=fieldnames)
                    if csv_reader:
                        for csv_row in csv_reader:
                            if csv_reader.line_num == 2:
                                self.clear()     
                            if csv_reader.line_num >= 2:
                                record = Record()
                                if record.import_data(csv_row):
                                    self.add_record(record)
                        result = True
            except (FileNotFoundError, ValueError):
                ...
        return result


    def _split_line_by_commas(self, line):
        parts = []
        current_part = ''
        inside_quotes = False

        for char in line:
            if char == ',' and not inside_quotes:
                parts.append(current_part.strip())
                current_part = ''
            elif char == '"':
                inside_quotes = not inside_quotes
            else:
                current_part += char

        parts.append(current_part.strip())
        return parts


    def backup_data(self, version=None, backup:bool = None) -> bool:
        if self.auto_backup or backup:
            if version:
                filename = f"{self.default_filename}_{version}.bin"
            else:
                filename = f"{self.default_filename}.bin"
            with open(self._gen_filename(filename), "wb") as file:
                pickle.dump(self, file)
            return True


    def restore_data(self, version=None, restore:bool = None) -> bool:
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


    def list_csv(self):
        filename = "*.csv"
        list_files = Path('.').glob(self._gen_filename(filename))
        result_version = []
        for found_file in list_files:
            result_version.append(self._clean_filename(found_file.name))
        return "\n".join(result_version) if any(result_version) else True
    

    def __str__(self) -> str:
        result = [ str(i) for i in self.data.values() ]
        return "\n".join(result)


    def __iter__(self):
        self._page_pos = 0
        return self


    def __next__(self) -> list[Record]:
        if self._page_pos < len(self.data.keys()):
            result = []
            idx_min = self._page_pos
            idx_max = self._page_pos + self.max_records_per_page
            #print(f"__next__ {idx_min=}, {idx_max=}")
            keys = list(self.data)[idx_min:idx_max]
            for key in keys:
                result.append(self.data[key])
            self._page_pos += self.max_records_per_page
            return result
        self._page_pos = 0
        raise StopIteration

    def congrats_in_days(self, *args):
        days = int(args[0])
        congrats_birthdays = []
        for user in self.data.values():
            birthday = user.birthday  
            if birthday:
                today = datetime.now().date()
                next_birthday = datetime(
                    today.year, birthday.value.month, birthday.value.day).date()
                if next_birthday < today:
                    next_birthday = datetime(
                        today.year + 1, birthday.value.month, birthday.value.day).date()
                days_to_birthday = (next_birthday - today).days
                if days_to_birthday <= days:
                    congrats_birthdays.append((user.name, next_birthday))
                    #congrats_birthdays.append(user.birthday.value.day)
        #return f"{', '.join(str(p) for p in congrats_birthdays)}"
        return  "\n".join(f"{name}: {date.strftime('%Y-%m-%d')}" for name, date in congrats_birthdays)




