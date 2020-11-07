"""
Программа выводит на экран числа от 1 до 100 включительно, с новой строки.

Если число кратно трём, то вместо этого числа программа выводит слово "zip"
Если чисто кратно пяти, то вместо этого числа выводится слово "zap"
Если число кратно пятнадцати, то вместо этого числа выводится слово "zip-zap"

Тебе может понадобиться цикл for и ветвления
"""

def do_zipzap():
    for range_element in range(0, 100):
        if(range_element) % 15 == 0:
            print('zip-zap')
        elif(range_element) % 3 == 0:
            print('zip')
        elif(range_element) % 5 == 0:
            print('zap')
        else:
            print(range_element)


if __name__ == '__main__':
    do_zipzap()
