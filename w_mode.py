# w mode - open the file for writing 'x' overwriting the file

fh= open("file2.txt",'wt')
fh.write("The file is overwritten using 'w' model in python. \n")
fh.write("Have a nice day!!")

fh.close()