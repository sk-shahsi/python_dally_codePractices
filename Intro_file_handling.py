file_handler = open("practice.txt",'rt')

#Read opration
#read() => read the contents of the file as str

content = file_handler.read()
#Closing a file => close()
file_handler.close()

print(content)
print(type(content))