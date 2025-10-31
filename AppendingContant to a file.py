#'a' mode => Append mode
fh = open("file11.txt",'at')
fh.write("\nThis is the first line of the file using 'a' mode.\n")
fh.write("\nThis is the second line of the file'\n'")
fh.write("'a' mode create the file if not already existing.\n")
fh.write("Good bye!!!!")

fh.close()