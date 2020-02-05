# -*- coding: utf-8 -*-

#ввод: (комманда) (*объекты)
# ввывод: к какой группе принадлежит команда

# ввод> идти домой
# выввод: go - комаанда, ["домой"] - объект

from commands import commands


input_data = input('>').split(' ')
cmd = input_data[0].lower()
objct = input_data[1::]


def find_cmd(**kwargs):     # Проверяет введённые данные и возвращает соотв. команду из commands.py
    for key, value in kwargs.items():
        if cmd in value:
            return key
        elif key == 'unknown command':
            return f'Неизвестная команда: {cmd}'


if __name__ == "__main__":
    print(find_cmd(**commands))
