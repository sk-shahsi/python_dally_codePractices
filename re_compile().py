import re

phoe = "alice-123456789, mark-8954671235, carlo-8974547612"
pattern =r"\d{10}"

pattern_compile = re.compile(pattern)
print(pattern_compile)

match_obj = re.findall(pattern_compile, phoe)
print(match_obj)