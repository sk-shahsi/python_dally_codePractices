# filter(function, sequence)

seq= [1,2,3,4,5]
odd = lambda x : x % 2 != 0
filtered_output = filter(odd,seq)
print(f" Odd number in the above sequence are: {list(filtered_output)}")

