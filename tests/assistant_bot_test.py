import sys
import unittest

try:
    sys.path.append("./")  
    from assistant_bot.class_fields import Birthday
    from assistant_bot.class_fields import Email
except ImportError :
    sys.path.append("../")  
    from assistant_bot.class_fields import Birthday
    from assistant_bot.class_fields import Email


class Test_Assistant_bot_BirthDay(unittest.TestCase):
    def test_birthday_data_format_EU(self):
        testcase = "12.03.2023"
        expected = "2023-03-12"
        self.assertEqual(
            str(Birthday(testcase)), expected
        )


    def test_birthday_data_format_ISO(self):
        testcase = "2023-03-12"
        expected = "2023-03-12"
        self.assertEqual(
            str(Birthday(testcase)), expected
        )     


    def test_birthday_data_format_wrong_01(self):
        testcase = "2023-33-12"
        with self.assertRaises(ValueError) as cm:
            Birthday(testcase)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), 'month must be in 1..12')
        
    def test_birthday_data_format_wrong_02(self):
        testcase = "33.11.1111"
        self.assertRaises(ValueError, Birthday, testcase)

class Test_Assistant_bot_Email(unittest.TestCase):

    def test_email_ok(self):
        testcase = "some@some.com"
        expected = "some@some.com"
        self.assertEqual(str(Email(testcase)), expected)


    def test_email_wrong_01(self):
        testcase = "some.some.com"
        with self.assertRaises(ValueError) as cm:
            Email(testcase)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), 'wrong email format')


    def test_email_wrong_02(self):
        testcase = "some@somecom"
        with self.assertRaises(ValueError) as cm:
            Email(testcase)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), 'wrong email format')
        



unittest.main()
