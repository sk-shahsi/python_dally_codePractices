import os

file_name = "practice.txt"
if os.path.exists("practice.txt"):
    print("The file exists")
else:
 print("File dose not exist")
