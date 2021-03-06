import keyword
"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное


def are_there_odd(nums_list):
    if any(num_element % 2 == 0 for num_element in nums_list):
        print('есть четное')
    else:
        print('отсутствует четное')

are_there_odd([1, 3, 3, 7])
are_there_odd([1, 2, 3, 4])

# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
age = 17


def sell_alcohol():
   print('продано')


sell_alcohol() if age > 21 else print('мы не продаем алкоголь несовершеннолетним')


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()

def is_keyword(word):
    if (keyword.iskeyword(word)):
        print(word + ' это ключевое слово')
    else:
        print(word + ' это ключевое слово')


is_keyword('def')


# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."

def get_type(data_to_detect_type):
    if(type(data_to_detect_type) == str):
        print('Это строка')
    if(type(data_to_detect_type) == int):
        print('Это число')
    if(type(data_to_detect_type) == bool):
        print('Это булевый')
    if(type(data_to_detect_type) == None):
        print('Это None')
    if(type(data_to_detect_type) == list):
        print('Это список')
    if(type(data_to_detect_type) == tuple):
        print('Это кортеж')
    if(type(data_to_detect_type) == set):
        print('Это мноожество')
    if(type(data_to_detect_type) == dict):
        print('Это словарь')

get_type('hhh')