#in the name of GOD
#SeyyedMahdiHassanpour
#smahdi1991@gmail.com
import random

i = 0
checklist = ''
password = ''
print(ord("0"))
print(ord("a"))
print(ord("A"))


def checklist_filler(rand):
    global checklist
    if str(rand) not in checklist:
        checklist += str(rand)
    return 0


def select_random():
    global password
    random_number = random.randint(0, 2)
    if random_number == 0:
        password += chr(random.randint(97, 122))
        checklist_filler(0)
    elif random_number == 1:
        password += chr(random.randint(65, 90))
        checklist_filler(1)
    else:
        password += chr(random.randint(48, 57))
        checklist_filler(2)
    return 0


def guarantee_randomness():
    global password
    if "0" not in checklist:
        password += chr(random.randint(97, 122))
        checklist_filler(0)
    elif "1" not in checklist:
        password += chr(random.randint(65, 90))
        checklist_filler(1)
    elif "2" not in checklist:
        password += chr(random.randint(48, 57))
        checklist_filler(2)
    else:
        select_random()
    return 0


def guarantee_rand():
    global i
    for i in range(0, 8):
        if i > 5:  # 5 is equal to: range(0,8)=8 - (number of sets-1)=2   =>8-2=6
            guarantee_randomness()
        else:
            select_random()
        i += 1
    print(password)
    return 0


counter = 0
while counter < 100:
    guarantee_rand()
    if "0" not in checklist or "1" not in checklist or "2" not in checklist:
        print("error")
    password = ''
    checklist = ''
    counter += 1
