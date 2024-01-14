print(42 == 42)

print(40 == 42)

print("hello" == "hello")

print("hello" == "Hello")

print("dog" != "cat")

print(42 == 42.0)

print(1==1.0>0.75)

print(2==2.0<1.5)

print(3<2<"2")

print(1<2<3)

print(1>2 and 2<3)

grade = 95
print(100 >= grade >= 80)

#explain
2+2 == 4 and not 2+2 == 5 and 2*2 == 2+2

5>4 or 3<4 and 5>5

print(2+2 == 4 and not 2+2 == 5 and 2*2 == 2+2)
#true and true and true
#true and true
#true

print(5>4 or 3<4 and 5>5)
#true or (true and false)
#true or false
#true
#true or true and false
#true and false
#false

response_code=201
match response_code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 300:
        print("Multiple Choices")

lang=input("What's the programming language you want to learn?")

match lang:
    case "Javascript":
        print("You can become a Web Developer.")
    case "Python":
        print("You can become a Data Scientist.")
    case "Solidity":
        print("You can become a Blockchain Developer.")
    case "PHP":
        print("You can become a Backend Developer.")
    case "Java":
        print("You can become a Mobile App Developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")