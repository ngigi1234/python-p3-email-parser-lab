# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        email_pattern = r"([a-z][a-z\d]*(\.[a-z\d]+)*@[a-z]+\.[a-z]+)"
        res = []
        email_list = re.finditer(email_pattern, self.email_addresses)
        for item in email_list:
            address = (item.group())
            if address not in res:
                res.append(address)
        res.sort()
        return res