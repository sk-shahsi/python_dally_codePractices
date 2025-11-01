import re
message = "The current Python version is 3.13 other previous version is 3.12,3.11"
#If Python is present in message


match_object = re.search('13',message)
print(match_object)
if re.search('13',message):
    print("found")
else:
    print("not found")

print(message[32:34])
