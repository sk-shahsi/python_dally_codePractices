import re
message = "The current Python version is 3.13 other previous version is 3.12,3.11"
match_object =re.search("[0-9][0-9]",message)
print(match_object)