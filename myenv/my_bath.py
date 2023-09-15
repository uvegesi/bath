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

#3 - 2nd iteration
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

#4
def int_to_second(hour, minute, second):
    return (hour * 3600) + (minute * 60) + second

def guest_spent_most_time():
    guest = []
    spent_max_time_in, spent_time_in, time_in, time_out = 0, 0, 0, 0
    found_time_in = False
    for i in range(len(entries_list)-2):
        if entries_list[i][0] == entries_list[i+1][0] and not found_time_in:
            time_in = int_to_second(entries_list[i][3], entries_list[i][4], entries_list[i][5])
            found_time_in = True
        elif entries_list[i][0] != entries_list[i+1][0] and found_time_in:
            time_out = int_to_second(entries_list[i][3], entries_list[i][4], entries_list[i][5])
            found_time_in = False
        if time_in and time_out:
            spent_time_in = time_out - time_in
            if spent_time_in > spent_max_time_in:
                spent_max_time_in = spent_time_in
                guest.clear()
                guest = [entries_list[i][0], spent_max_time_in]
                                
    return(guest)

#print(guest_spent_most_time())

#5

def num_of_guest_in_periods(in_hour, in_min, in_sec, out_hour, out_min, out_sec):
    count = 0
    for i in range(len(entries_list) - 2):
        if entries_list[i][0] == entries_list[i+1][0] and entries_list[i][1] == 0 and entries_list[i][2] == 1:
            if in_hour <= entries_list[i][3] <= out_hour:
                if in_min <= entries_list[i][4] <= out_min:
                    if in_sec <= entries_list[i][5] <= out_sec:
                        count += 1
    print(f'{count} guest arrived to the bath between {in_hour} and {out_hour +1}.')

num_of_guest_in_periods(6, 0, 0, 8, 59, 59)
num_of_guest_in_periods(9, 0, 0, 15, 59, 59)
num_of_guest_in_periods(16, 0, 0, 19, 59, 59)

#6

def sec_to_int(sec):
    hour = sec // 3600
    min = (sec % 3600) // 60
    sec = sec % 60
    return [hour, min, sec]

def in_the_sauna():
    #guests_in_sauna = []
    in_sauna = list(filter(lambda x: x[1] == 2, entries_list))
    for i in range(0, len(in_sauna), 2):
        time_spent = sec_to_int(abs(int_to_second(in_sauna[i][3], in_sauna[i][4], in_sauna[i][5]) - 
                         int_to_second(in_sauna[i+1][3], in_sauna[i+1][4], in_sauna[i+1][5])))      
        #guests_in_sauna.append([in_sauna[i][0], time_spent[0], time_spent[1], time_spent[2]])
        print(f'{in_sauna[i][0]} - {time_spent[0]}:{time_spent[1]}:{time_spent[2]}')
        print(in_sauna[i][0],'-', ':'.join((map(lambda x: str(x), time_spent))))
        print(in_sauna[i][0],'-', ':'.join((map(str, time_spent))))
    
in_the_sauna()

print(int_to_second(7, 18, 52))
print(sec_to_int(26332))

#7
def return_guest_only(entry, pool):
    if pool in entry:
        return entry[0]

def guests_per_pools():
    pool_list = list(set(map(lambda x: x[1], entries_list)))
    guests_pool = []
    for pool in pool_list:
        guest_set = set(map(lambda entry: return_guest_only(entry, pool), entries_list))
        guests_pool.append([pool, guest_set])
    
    print(guests_pool)
    
guests_per_pools()

#7b

def guests_per_pools_2():
    pool_set = set(map(lambda x: x[1], entries_list))
    guests_in_pools = []
    for pool in pool_set:
        guest_set = set()
        for entry in entries_list:
            if entry[1] == pool:
                guest_set.add(entry[0])
        guests_in_pools.append([pool, guest_set])
    
    for i in range(5):
        print(guests_in_pools[i][0], len(guests_in_pools[i][1]))
    
guests_per_pools_2()