
import re
s1 = "Python is programming language python3.13"

#[A-Z][a-z]

# pat = r"old\new"
pat = r"[A-Z][a-z][a-z]"
match_object = re.search(pat, s1)

print(match_object)

#\d and \D
#\d matches 1 digit character> It is similer to [0-9]

pat = r"[a-z][a-z][a-z]\d"
match_object = re.search(pat, s1)
print(match_object)

#\d and \D
#\d matches 1 digit character> It is similer to [0-9]

pat = r"[a-z][a-z][a-z]\D"
match_object = re.search(pat, s1)
print(match_object)


#\s, \S
#\s matches aby whitespace character
#\d and \D
#\d matches 1 digit character> It is similer to [0-9]

pat = r"[a-z][a-z][a-z]\s"
match_object = re.search(pat, s1)
print(match_object)
s2 = """ Hello there 
We are Learning Python

"""
#\d and \D
#\d matches 1 digit character> It is similer to [0-9]

pat = r"[a-z][a-z][a-z]\s"
match_object = re.search(pat, s2)
print(match_object)