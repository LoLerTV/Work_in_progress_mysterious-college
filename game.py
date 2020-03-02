
import get_data
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
