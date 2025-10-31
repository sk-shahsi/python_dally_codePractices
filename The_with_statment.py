# fh = open("practical_1.txt",'rt')
# content = fh.read()
# fh.close()
#
# print(content)

with open("practical22.txt",'xt')as fh:
   """ content = fh.read()
    print(content)
    """
   fh.write("New file creation\n")
   fh.write("Bye")

