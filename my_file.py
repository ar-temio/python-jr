fruits = ["яблоко","банан","апельсин"," киви"]

# fruits.append("манго")
# 
# 
# fruits.sort()
# 
# 
# print("Сортированные фрукты:")
# for fruit in fruits:
#     print(fruit)
# 
# 
# first_ftuit = fruits[0]
# print(f"Первый фрукт в списке: {first_ftuit}")

container = ["молоко", "мороженное", "каша", "суп", "арбузик"]

for a in container:
    fruits.append(a)

print(fruits)

for i in range(len(fruits)):
    if fruits[i] == "каша":
        fruits.pop(i)
    
print(fruits)


# fruits.append("молоко")
# fruits.append("мороженное")
# fruits.append("каша")
# fruits.append("суп")
# fruits.append("арбузик")

# for fruit in fruits:
#     print(fruit)
#     if fruit == "мороженное":
#         print("КУПИ ПАПЕ")
