'''Первая задача'''
def custom_sort(lst):
    n = len(lst)

    two_thirds_index = n * 2 // 3
    one_third_index = n // 3

    average = sum(lst) / n

    if average > 0:

        sorted_part = sorted(lst[:two_thirds_index])
        unsorted_part = lst[two_thirds_index:]
    else:
        sorted_part = sorted(lst[:one_third_index])
        unsorted_part = lst[one_third_index:]

    return sorted_part + unsorted_part[::-1]


example_list = [3, -1, 4, -2, 5, 0, -3, 2]
result = custom_sort(example_list)
print(result)

'''Вторая задача'''

score = []
for i in range(1, 11):
    b = 0
    while b < 1 or b > 12:
        b = int(input(f'{i} оценка: '))
    score.append(b)

option = 0
while option == 0:
    print('\n1. Вывод списка оценок', '2. Пересдача экзамена', '3. Выходит ли стипендия',
          '4. Сортировка оченок по возрастанию', '5. Сортировка оченок по убыванию', '6. Выход', '\n', sep='\n')
    option = int(input())
    if option == 1:
        print(*score)
    elif option == 2:
        index = int(input('Введите номер экзамена: '))
        otsenka = int(input('Введите оценку: '))
        if otsenka > 0 and otsenka < 13:
            score[index - 1] = otsenka
            print('Оценка изменена')
    elif option == 3:
        if sum(score) / len(score) >= 10.7:
            print('Стипендия выходит')
        else:
            print('Стипендия не выходит')
    elif option == 4:
        score.sort()
        print(*score[::-1])
    if option != 6:
        option = 0

"""Третья задача"""


def bubble_sort(lst):
    n = len(lst)

    for i in range(n - 1):
        swaps = 0

        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swaps += 1

        if swaps == 0:
            break


    return lst

numbers = [2 ,5, 12, 6, 9, 0, -1, 4]
print(bubble_sort(numbers))
