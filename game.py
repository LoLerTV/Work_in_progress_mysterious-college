# -*- coding: utf-8 -*-


from commands import commands
import transitions

class Room:
    """Класс моделирующий комнату"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []


class Player:
    """Player"""
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []



scheduling= Room(transitions.scheduling_room[0],transitions.scheduling_room[1])


player = Player("Игрок", scheduling)


#Start
print("Таинственный колледж")
print("\n")
print("""Ох блин… Всё болит… Голова раскалывается… 
Всё трясётся… Я ничего не вижу… Ох… Стоп, как я сюда попал? 
И куда это сюда?""")


while True:
 
    #get command
    # ввод: (комманда) (*объекты)
    # ввывод: к какой группе принадлежит команда
    # ввод: идти в дом
    # выввод: go - команда(таким образом "идти" и "пойти" - одно и то же), ["в", "домой"] - объект

    input_data = input('>').split(' ')
    cmd = input_data[0].lower()
    objct = input_data[1::]

    
    def find_cmd(**kwargs):     # Проверяет введённые данные и возвращает соотв. команду из commands.py 
        for key, value in kwargs.items():
            if cmd in value:
                return key
            elif key == 'unknown command':
                return f'Неизвестная команда: {cmd}'


    if find_cmd(**commands) == "unknown command":
        print(find_cmd(**commands))


    #Осмотреться
    if find_cmd(**commands) == "look_around":
        print('Это', player.location.name)
        print(player.location.description)
        print("Здесь есть: ")
        for item in player.location.items:
            print(item)
        print("Отсюда можно пойти в: ")
        for exit_in in player.location.exits:
            print(exit_in)

    



    
    