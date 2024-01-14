snacks = ["mars", "lays", "oreo"]
print(snacks)

snacks = ["mars", "lays", "oreo"]
print(snacks[0])
print(snacks[1])
print(snacks[2])
print(snacks[-1])

snacks = ["mars", "lays", "oreo"]
snacks[0] = "galaxy"
print(snacks)

snacks = ["mars", "lays", "oreo"]
snacks.append("galaxy")
print(snacks)

snacks = ["mars", "lays", "oreo"]
snacks.insert(3,"galaxy")
snacks.insert(0,"doritos")
snacks.insert(1,"coke")
print(snacks)

snacks = ["mars", "lays", "oreo"]
print(snacks)   
popped_snacks = snacks.pop()
print(snacks)
print(popped_snacks)
first_snack = snacks.pop(0)
print("The first snack is :", first_snack)

snacks = ["mars", "lays", "oreo"]
print(snacks)
snacks.remove("lays")
print(snacks)

snacks = ["mars", "lays", "oreo"] 
snacks.sort()
print(snacks)
snacks.sort(reverse=True)
print(snacks)

snacks = ["mars", "lays", "oreo"]
sorted(snacks)
sorted(snacks, reverse=True)

snacks = ["mars", "lays", "oreo"]
print(snacks)
print("\nHere is the sorted list in alphabetical order:")
print(sorted(snacks))
print("\nHere is the sorted list in reverse alphabetical order:")
print(sorted(snacks, reverse=True))
print("\nHere is the original list again:")
print(snacks)

snacks = ["mars", "lays", "oreo"]
for snacks in snacks:
    print(snacks)

snacks = ["mars", "lays", "oreo"]
snacks.reverse()
print(snacks)

snacks = ["mars", "lays", "oreo"]
print(len(snacks))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
a_zip = zip(list1, list2)
zipped_list = list(a_zip)
print(zipped_list)