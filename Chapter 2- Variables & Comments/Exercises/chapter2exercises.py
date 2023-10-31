#Exercise 1: Variables
M = ("I want to Sleep")
print(M)
M = ("One More Episode")
print(M)

#Exercise 2: Variables
print("Master Shifu once said, “If you only do what you can do\nyou can never be more than you are.")

#Exercise 3: Stripping Names
a = "\tCyrus DS\n"
print(a)
print(a.lstrip())
print(a.rstrip())
print(a.strip())

#Exercise 4: Favorite Number
favnum = int(input("What is your favorite number? "))
print("Your Favorite number is", favnum)

#Exercise 5: USB Shopper
usb_girl = ("USB Sticks she can buy = ")
pounds_left = ("Pounds she will have left = ")
print(usb_girl + str(int(50/6)))
print(pounds_left + str(50%6))