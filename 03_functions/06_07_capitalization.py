# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text. 7. Продолжить работу над заданием. В программу должна
# попадать строка из слов, разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно
# сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее
# функцию int_func().

def int_func():
    words = str(input('Enter lowercase words: '))
    tokens = words.split(" ")
    capitalized_words = []
    for i in tokens:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        capitalized_words.append(word)
    return capitalized_words


print(int_func())
