languages = ["Swift", "Python", "Go", "Javascript"]
for language in languages:
  print(language)

values = range(4)
for i in values:
  print(i)

languages = ["Swift", "Python", "Go"]
for language in languages:
  print("Hello")
  print("Hi")

digits = [0, 1, 5]
for i in digits:
  print(i)
else:
    print("No items left.")

i = 1
n = 5
while i <= n:
  print(i)
  i = i+1

total = 0
number = int(input("Enter a number: "))
print("total =", number)
while number != 0:
      number = int(input("Enter another number: "))
      total += number
      print("total =", total)
