import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

# line 7 passes tests 1 and 2
# name = r"([\w.-]+)\s([\w.-]+)"
# line 9 passes tests 1 through 4
# name = r"([\w.-]+)[\s|\S]([\w.-]+)"
name = r"[A-Z][a-zA-Z'-]+(?:\s[A-Z][a-zA-Z'-]+)?"
name_regex = re.compile(name)

phone_number = r"(\d{10})|(\(\d{3}\)\s\d{3}-\d{4})|(\d{3}-\d{3}-\d{4})"
phone_regex = re.compile(phone_number)

email_address = r"^[A-Za-z][\w.-]*@[A-Za-z]+\.[A-Za-z]+$"
email_regex = re.compile(email_address)
