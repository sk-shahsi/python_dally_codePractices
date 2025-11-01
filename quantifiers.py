import re
message = "The current Python version is 3.13 other previous version is 3.12,3.11"

pat = r"[a-z] {4}"
match_object = re.search(pat, message)
print(match_object)


pat = r"[A-Z][a-z]{5}"
match_object = re.search(pat, message)
print(match_object)

# ^ - Caret
s1= "Python is a programing Language"
pat = r"[a-z]{8}"
match_object = re.search(pat, s1)
print(match_object)

# $ - doller

s2= "Python is a programing Language"
pat = r"[a-z]{8}"
match_object = re.search(pat, s2)
print(match_object)


#group -()
emails = "abc@gmail.com random words and characters. x1y2z3.abc.edu"


pat = r"[com]"
match_object = re.search(pat, emails)
print(match_object)