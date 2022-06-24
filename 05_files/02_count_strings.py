# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
# строке.

i = 0
str1 = ""

with open("02_count_strings.txt") as lorem:
    lines = 0
    for line in lorem:
        lines += line.count("\n")
        i += 1
        words_in_line = len(line.split())
        str1 = str1 + "Слов в строке № " + str(i) + ": " + str(words_in_line) + "\n"
    print(f"Всего строк: {lines}")

print('\n' + str1)
