def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    a = []
    for i in names:
        a.append(f"Hello, my name is {i}.")

    return a

def assign_rooms(names):
    a = []
    sum = 1
    for i in names:
        a.append(f"Hello, {i}! You'll be assigned to room {sum}!")
        sum += 1

    return a

def printer(names):
    #print(batch_badge_creator(names))
    #print(assign_rooms(names))
    for i in batch_badge_creator(names):
        print(i)
    
    for i in assign_rooms(names):
        print(i)




printer(["Arel", "Carol"])