from get_data import *

scheduling_room = ('Комната с рассписанием', 'Ты в небольшой, хорошо освещённой комнате c рассписанием каких то предметов и звонков. Перед тобой дверь в коридор.')
corridor = ('Коридор', 'Ты длинном корридоре. Справа ты видишь ряд дверей. На одной из них написанно "столовая".')
canteen = ('Столовая','Ты в столовой. Справа от тебя буфет, слева столики а спереди огромное окно.')

transitions = {
    scheduling_room: (corridor),
    corridor: (canteen, scheduling_room),
    canteen: (corridor)
}

location = scheduling_room

print(transitions[scheduling_room][0])
print(transitions[scheduling_room][1])
