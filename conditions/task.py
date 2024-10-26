name = input(" enter your name -") 

action = input("chto delat? ")
a = int(input("a = "))
b = int(input("b = "))

if action == "summa":
    rezult = a + b

if action == "raznost":
    rezult = a - b

if action == "umnojenie":
    rezult = a * b 

print(f"{name} tvoi rezult = {rezult}")
