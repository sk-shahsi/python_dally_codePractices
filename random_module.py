import random
#random() -return random float between 0.0 and 1.0(excluded)
print(random.random())

#randint(a,b)=> return random init between a and b (booth included)
print(random.randint(1,10))

#choice(sequence) => return a random ite from the sequence
print(random.choice("abcdefghijklmnopqrst"))

#suffle(sequence)=> return the element the suffle in rrendom
fruits=["apple","banana","orange","cherry"]
random.shuffle(fruits)
print(fruits)