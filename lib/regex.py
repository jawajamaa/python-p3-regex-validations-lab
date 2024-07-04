import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

# line 7 passes tests 1 and 2
# name = r"([\w.-]+)\s([\w.-]+)"
# line 9 passes tests 1 through 4
# name = r"([\w.-]+)[\s|\S]([\w.-]+)"
name = r"([\w.-]+)[\s|\S]([\w.-]+)"
name_regex = re.compile(name)

phone_number = r""
phone_regex = re.compile(phone_number)

email_address = r""
email_regex = re.compile(email_address)
