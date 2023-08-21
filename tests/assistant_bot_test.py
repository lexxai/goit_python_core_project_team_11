import sys
import unittest

try:
    sys.path.append("./")
    from assistant_bot.class_fields import Birthday
    from assistant_bot.class_fields import Email
    from assistant_bot.class_fields import Phone
except ImportError:
    sys.path.append("../")
    from assistant_bot.class_fields import Birthday
    from assistant_bot.class_fields import Email
    from assistant_bot.class_fields import Phone


class Test_Assistant_bot_BirthDay(unittest.TestCase):
    def test_birthday_data_format_EU(self):
        testcase = "12.03.2023"
        expected = "2023-03-12"
        self.assertEqual(str(Birthday(testcase)), expected)

    def test_birthday_data_format_ISO(self):
        testcase = "2023-03-12"
        expected = "2023-03-12"
        self.assertEqual(str(Birthday(testcase)), expected)

    def test_birthday_data_format_ISO_SL(self):
        testcase = "12/03/2023"
        expected = "2023-03-12"
        self.assertEqual(str(Birthday(testcase)), expected)

    def test_birthday_data_format_wrong_01(self):
        testcase = "2023-33-12"
        with self.assertRaises(ValueError) as cm:
            Birthday(testcase)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "month must be in 1..12")

    def test_birthday_data_format_wrong_02(self):
        testcase = "33.11.1111"
        self.assertRaises(ValueError, Birthday, testcase)

    def test_birthday_data_format_wrong_03(self):
        testcase = ""
        self.assertRaises(ValueError, Birthday, testcase)

    def test_birthday_data_format_wrong_04(self):
        testcase = "2020/11/11"
        self.assertRaises(ValueError, Birthday, testcase)


class Test_Assistant_bot_Email(unittest.TestCase):
    def test_email_ok(self):
        testcase = "some@some.com"
        expected = "some@some.com"
        self.assertEqual(str(Email(testcase)), expected)

    def test_email_wrong_01(self):
        testcase = "some.some.com"
        self.assertRaises(ValueError, Email, testcase)

    def test_email_wrong_02(self):
        testcase = "some@somecom"
        self.assertRaises(ValueError, Email, testcase)

    def test_email_wrong_03(self):
        testcase = "some#some.com"
        self.assertRaises(ValueError, Email, testcase)

    def test_email_wrong_03(self):
        testcase = ""
        self.assertRaises(ValueError, Email, testcase)


class Test_Assistant_bot_Phone(unittest.TestCase):
    def test_phone_OK_01(self):
        testcase = "4423"
        expected = "4423"
        self.assertEqual(str(Phone(testcase)), expected)

    def test_phone_OK_02(self):
        testcase = "+380441234123"
        expected = "+380441234123"
        self.assertEqual(str(Phone(testcase)), expected)

    def test_phone_OK_03(self):
        testcase = "+380(44)1234123"
        expected = "+380(44)1234123"
        self.assertEqual(str(Phone(testcase)), expected)

    def test_phone_OK_04(self):
        testcase = "+380(44)123-1234"
        expected = "+380(44)123-1234"
        self.assertEqual(str(Phone(testcase)), expected)

    def test_phone_OK_05(self):
        testcase = "123-1234-123"
        expected = "123-1234-123"
        self.assertEqual(str(Phone(testcase)), expected)

    def test_phone_OK_06(self):
        testcase = "1231234123"
        expected = "1231234123"
        self.assertEqual(str(Phone(testcase)), expected)

    def test_phone_OK_07(self):
        testcase = "+48123123412"
        expected = "+48123123412"
        self.assertEqual(str(Phone(testcase)), expected)

    def test_phone_OK_08(self):
        testcase = "+48 12 1234123"
        expected = "+48 12 1234123"
        self.assertEqual(str(Phone(testcase)), expected)

    def test_phone_wrong_01(self):
        testcase = "48123123412"
        self.assertRaises(ValueError, Phone, testcase)

    def test_phone_wrong_02(self):
        testcase = "+48123123"
        self.assertRaises(ValueError, Phone, testcase)

    def test_phone_wrong_03(self):
        testcase = "A48123123"
        self.assertRaises(ValueError, Phone, testcase)

    def test_phone_wrong_04(self):
        testcase = "+380.44.123.1234.123"
        self.assertRaises(ValueError, Phone, testcase)

    def test_phone_wrong_05(self):
        testcase = ""
        self.assertRaises(ValueError, Phone, testcase)

    def test_phone_wrong_06(self):
        testcase = "+38050123412"
        self.assertRaises(ValueError, Phone, testcase)

    def test_phone_wrong_07(self):
        testcase = "+48034567892"
        self.assertRaises(ValueError, Phone, testcase)

    def test_phone_wrong_08(self):
        testcase = "+38991234123"
        self.assertRaises(ValueError, Phone, testcase)


# run by pytest 3
if "__main__" == "assistant_bot_test":
    unittest.main()
elif "__main__" == "__main__":
    print("for test need run 'pytest'")
