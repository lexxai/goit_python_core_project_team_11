import sys
import unittest

try:
    sys.path.append("./")  
    #from assistant_bot.class_assistant_bot import Assistant_bot
    from assistant_bot.class_fields import Birthday
    #from assistant_bot.main import cli      
except ImportError :
    sys.path.append("../")  
    #from assistant_bot.class_assistant_bot import Assistant_bot
    from assistant_bot.class_fields import Birthday
    #from assistant_bot.main import cli


class Test_Assistant_bot(unittest.TestCase):
    def test_birthday_data_format(self):
        testcase = "12.03.2023"
        expected = "2023-03-12"
        self.assertEqual(
            str(Birthday(testcase)), expected
        )


unittest.main()
