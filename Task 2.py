# На вход функция получает список из целых чисел.
# Результатом работы функции должен стать новый список, в котором содержатся только те числа, которые больше 5.

numbers = input("Введите список чисел через пробел: ").split()
#numbers = [int(num) for num in numbers] #значению num in numbers=int

def all_num(number):
    all_numbers = []
    for number in numbers:
        if int(number) > 5:
            all_numbers += [number]
    return all_numbers


print(all_num(numbers))
