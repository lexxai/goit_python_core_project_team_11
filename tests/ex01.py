
import re
 
test_str = '24.08.1997'
pattern_str = r'^\d{2}.\d{2}.\d{4}$'
 
if re.match(pattern_str, test_str):
    print("True")
    new_test = test_str[6:]+"/"+test_str[3:5]+"/"+test_str[0:2]
    print(new_test)
else:
    print("False")

