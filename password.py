"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""


def pass_check(password):
    password_is_hard = False
    if any(password_symbol.isdigit() for password_symbol in password):
        if any(password_symbol.isalpha() for password_symbol in password):
            if len(password) > 7:
                password_is_hard = True

    print('сложный' if password_is_hard else 'простой')


if __name__ == '__main__':
    pass_check(input('нужно передать пароль: '))
