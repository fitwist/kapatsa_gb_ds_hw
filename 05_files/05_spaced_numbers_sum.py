# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить её на экран.

numbers = []
numbers_lst = []

while True:
    line = input("Введите число: ")
    if line == '':
        print(numbers)
        break
    else:
        newline = line + ' '
        numbers_lst.append(line)
        numbers.append(newline)

    with open("05_spaced_numbers_sum.txt", "w") as file_obj:
        file_obj.writelines(numbers)

avg = sum(map(float, numbers_lst)) / len(numbers_lst)
print(f'Средний оклад: {avg}')
