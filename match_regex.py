import re
s1 = "We are learning rgex in Python"

pat = r"[a-z]{5}"

match_object = re.search(pat, s1)
print(match_object)

phone = "jom-12345678910, carlo-98745612350, mark-5698742156"
pat = r"[0-9]{10}"
match_object = re.findall(pat, phone)
print(match_object)