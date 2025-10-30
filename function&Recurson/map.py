seq=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#mapeed_output = map(lambda x: True if x % 2 !=0 else False,seq)
mapeed_output = map(lambda x: x ** 2, seq)
print(mapeed_output)
print(f"{list(mapeed_output)})")