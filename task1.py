container = []

container.append("dad")
container.append("mom")
container.append("son")

print(container)

while True:
    element = input("введите элемент списка ")

    if element == "STOP":
        break
    container.append(element)

print(container)
