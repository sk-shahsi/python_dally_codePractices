p="buy now"
p1="click now"
p2="click the link now"

msage=input("write your comment here ")
if((p in msage) or(p1 in msage) or(p2 in msage)):
    print("this comment is spam")

else:
    print("comment posted ",msage)