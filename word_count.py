countries =["India", "USA", "Canada","Brazil", "China", "China",
            "Iran","Poland","Cuba"]
# Count all the counteries which are starting with I
counter = 0
for country in countries:
    if country[0] == "I":
        counter = counter +1
        print(counter)


for cou in countries:
   if cou.startswith("I"):
       counter = counter +1
       print("Count countery start with",counter)
