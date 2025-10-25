def sum(n):
    if(n==1 ):
      return 1
    return sum(n-1) + n
print(sum(2))
# n=int(print( "give a number"))