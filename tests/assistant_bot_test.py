import sys
import unittest

try:
    sys.path.append("./")  
    from assistant_bot.class_fields import Birthday
except ImportError :
    sys.path.append("../")  
    from assistant_bot.class_fields import Birthday


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
        self.assertNotEqual(the_exception, "ValueError('month must be in 1..12')")



unittest.main()
