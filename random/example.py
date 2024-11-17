import random

result = random.randint(0, 10)

while True:
    answer = int(input("Введите ваш отвтет -> "))
    if answer == result:
        print("Вы угадали!")
        break
    else:
        print("Попробуйте еще раз!")
