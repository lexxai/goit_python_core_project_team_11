from datetime import date
import re


# Parent class
class Field:
    def __init__(self, value: any) -> None:
        self.__value = value
        self.value = value

    def search(self, pattern: str, case=False) -> bool:
        value = str(self.value)
        if not case:
            pattern = pattern.lower()
            value = value.lower()
        return value.find(pattern) != -1

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, __new_value):
        if __new_value and __new_value.isprintable():
            self.__value = __new_value
        else:
            raise ValueError("used non printable chars")

    def __eq__(self, __other):
        if isinstance(__other, Field):
            return self.value == __other.value
        else:
            raise TypeError

    def __repr__(self):
        return str(self)

    def __str__(self) -> str:
        return str(self.__value) if self.__value else ""


# Child classes
class Name(Field):
    ...


class Address(Field):
    ...


class Email(Field):
    def find_all_emails(self, text):
        result = re.findall(r"[a-zA-Z][\w_.]+@\w{2,}\.\w{2,}", text)
        return result

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, __new_value):
        result = self.find_all_emails(__new_value)
        if result:
            self.__value = __new_value
        else:
            raise ValueError("wrong email format")


class PhoneCodes:
    code_numbers_length: dict = {"380": 12, "48": 11, "38": 0, "7": 0}

    @staticmethod
    def detect_number_length(phone_number: str) -> int:
        min_length = 10
        max_length = 15
        if phone_number.startswith("+"):
            phone_number_code = phone_number[1:5]
            for code, length in PhoneCodes.code_numbers_length.items():
                if phone_number_code.startswith(code):
                    first_local_number = phone_number[len(code) + 1]
                    # print(f"***** {first_local_number=}")
                    if first_local_number == "0":
                        min_length, max_length = (0, 0)
                        break
                    if isinstance(length, tuple):
                        min_length, max_length = length
                    else:
                        min_length = length
                        max_length = length
                    break
        # print(f"{phone_number_code=}", min_length, max_length)
        return min_length, max_length


class Phone(Field):
    def phone_length(self, test_str: str) -> int:
        """Calculate length of string of digitals only chars

        Args:
            test_str (str): _description_

        Returns:
            int: _description_
        """
        regex = r"([^\d]?)"
        subst = ""
        length = len(re.sub(regex, subst, test_str, 0))
        # print(f"{length=}")
        return length

    def is_phone(self, test_str: str) -> bool:
        # print(f"is_phone {test_str=}")
        # Intonational format of phone ?
        if test_str.startswith("+"):
            phone_len = self.phone_length(test_str)
            min_length, max_length = PhoneCodes.detect_number_length(test_str)
            if phone_len > max_length or phone_len < min_length:
                return False
        else:
            if self.phone_length(test_str) > 10:
                return False
        # allow only digit, space, ( , ) , -
        regex = r"^\+?[\d\s\-\(\)]+$"
        matches = re.search(regex, test_str)
        return matches is not None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, __new_value):
        if self.is_phone(__new_value):
            self.__value = __new_value
        else:
            raise ValueError("wrong phone format")


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, __new_value):
        new_date = __new_value
        pattern_str = r"^\d{2}.\d{2}.\d{4}$"
        if re.match(pattern_str, __new_value):
            new_date = __new_value[6:] + "-" + __new_value[3:5] + "-" + __new_value[0:2]
        d = date.fromisoformat(new_date)
        # print(f"date= {d}")
        if d:
            self.__value = d
        else:
            raise ValueError("wrong date format, not ISO 8601")

    def __str__(self):
        value = self.__value
        result = value.isoformat() if value else ""
        return result


class Tag(Field):
    ...


class Note(Field):
    ...
