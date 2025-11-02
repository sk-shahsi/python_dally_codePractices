import re

#sub()

s1 = "sunday, Monday, Tuesday, Thursday, Friday, Saturday, Sunday"
replace_obj = "Sunday"
pat=r"S[a-z]+"
replace_object = re.sub(pat, replace_obj, s1)
print(replace_object)
