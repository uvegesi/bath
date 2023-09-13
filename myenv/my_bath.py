import os

#1
print("Current working directory:", os.getcwd())

entries = open('furdoadat.txt')

entries_list = []
for entry in entries:
    entry = list(map(int, entry.split()))
    entries_list.append(entry)
    
print(entries_list)

#2
def first_last_in_changingroom(lista):
    first_guest = entries_list[0][0]
    last_guest = entries_list[len(entries_list)-1][0]
    for item in lista:
        if first_guest in item or last_guest in item:
            if item[1] == 0 and item[2] == 1:
                print(item[3],':',item[4],':',item[5], sep='')

first_last_in_changingroom(entries_list)

#3
guests_set = set(map(lambda x: x[0], entries_list))
print(guests_set)

def guest_in_one_room():
    one_guest = []
    guests = []
    visiting_set = set()
    for i in range(len(entries_list) -2):
        if entries_list[i][0] not in one_guest:
            one_guest.append(entries_list[i][0])
        if entries_list[i][0] == entries_list[i+1][0]:
            visiting_set.add(entries_list[i+1][1])
        else:  
            one_guest.append(visiting_set)
            print('one guest:', one_guest)
            guests.append(one_guest)
            one_guest = []
            visiting_set = set()
    print('guests', guests)

    print('This is the final list:', len(list(filter(lambda x: len(x[1]) == 2, guests))))
    print()

    #print(guests)
    
guest_in_one_room()

#2/b

def guest_in_one_room2():
    guests = []
    visiting_set = set()
    for i in range(len(entries_list) -2):
        if entries_list[i][0] == entries_list[i+1][0]:
            visiting_set.add(entries_list[i+1][1])
        else:
            if len(visiting_set) == 2:
                guests.append(entries_list[i][0])
            visiting_set = set()
            
    return len(guests)
            
print(guest_in_one_room2())