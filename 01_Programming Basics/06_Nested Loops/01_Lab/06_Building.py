floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    buff = ""
    for room in range(rooms):
        if floor == floors:
            buff += f"L{floor}{room} "
        elif floor % 2 == 0:
            buff += f"O{floor}{room} "
        elif floor % 2 != 0:
            buff += f"A{floor}{room} "

    print(buff)
