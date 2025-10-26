score=[2,45,102,4,9,12,90,1,0,1]
print(score)
total=0
for s in score:
    total= total + s
print("Total number add is :",total)


total = sum(score)
print(total)

#find higest score
higest=score[0]
for s in score:
    if higest < s:
        higest = s

print("higest score is :",higest)

lowest=min(score)
print("lowest score is :",lowest)
low=score[0]
for scores in score:
    if scores <low:
        low = scores
print("lowest score is :",lowest)