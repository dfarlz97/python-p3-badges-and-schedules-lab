def badge_maker(name):
    badge = f"Hello, my name is {name}."
    return badge

def batch_badge_creator(names):
    index = 0 
    badge_list = list()
    for name in names: 
        badge_list.append(f"Hello, my name is {names[index]}.")
        index += 1 
    return badge_list

def assign_rooms(names):
    index = 0 
    count = 1
    room_list = list()
    for name in names:
        room_list.append(f"Hello, {names[index]}! You'll be assigned to room {count}!")
        index += 1
        count += 1
    return room_list

def printer(names):
    index = 0 
    count = 1 
    index2 = 0
    count2 = 1
    for name in names:
        print(f'Hello, my name is {names[index]}.')
        index += 1
        count += 1
    for name in names: 
        print(f"Hello, {names[index2]}! You'll be assigned to room {count2}!")
        index2 += 1
        count2 += 1
