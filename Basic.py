import random

attempt = False
attempt2 = False
while attempt is False:
    try:
        p1_name = input('Player 1: ')
        p1_HP = int(input('HP: '))
        p1_AC = int(input("AC: "))
        attempt = True
    except ValueError:
        print("Invalid value")

while attempt2 is False:
    try:
        p2_name = input('Player 2: ')
        p2_HP = int(input("HP: "))
        p2_AC = int(input("AC: "))
        attempt2 = True
    except ValueError:
        print("Invalid value")
print(f'{p1_name} vs. {p2_name}')
print(' ')
print('FIGHT')
p1_temp_AC = 0
p2_temp_AC = 0
p1_com = ''
p2_com = ''

while True:
    if p1_HP > 0:
        p1_temp_AC = 0
        print(' ')
        p1_com = input(f"{p1_name}, type a command> ")
        if p1_com.lower() == 'attack':
            print(f'{p1_name} attacks!')
            atk = random.randint(1, 20)
            if atk >= p2_AC and atk >= p2_temp_AC:
                dmg = random.randint(1, 6)
                print(f'{p2_name} takes {dmg} damage')
                p2_HP -= dmg
                print("Ouch!")
            else:
                print(f'{p1_name} missed')
        elif p1_com.lower() == 'defend':
            print(f'{p1_name} prepares for an incoming attack')
            if p1_temp_AC == 0:
                p1_temp_AC = p1_AC + 3
            else:
                pass
        elif p1_com.lower() == 'run':
            print(f'{p1_name} chickened out ...')
            print(' ')
            print(' ')
            print(f'***** {p2_name} WINS *****')
            break
        else:
            print(f"Invalid input, guess it's {p2_name}'s turn!")
    else:
        print(' ')
        print(' ')
        print(f'***** {p2_name} WINS *****')
        break
    if p2_HP > 0:
        p2_temp_AC = 0
        print(' ')
        p2_com = input(f"{p2_name}, type a command> ")
        if p2_com.lower() == 'attack':
            print(f'{p2_name} attacks!')
            atk = random.randint(1, 20)
            if atk >= p1_AC and atk >= p1_temp_AC:
                dmg = random.randint(1, 6)
                print(f'{p1_name} takes {dmg} damage')
                p1_HP -= dmg
                print("Ouch!")
            else:
                print(f'{p2_name} missed')
        elif p2_com.lower() == 'defend':
            print(f'{p2_name} prepares for an incoming attack')
            if p2_temp_AC == 0:
                p2_temp_AC = p2_AC + 3
            else:
                pass
        elif p2_com.lower() == 'run':
            print(f'{p2_name} chickened out ...')
            print(' ')
            print(' ')
            print(f'***** {p1_name} WINS *****')
            break
        else:
            print(f"Invalid input, guess it's {p1_name}'s turn!")
    else:
        print(' ')
        print(' ')
        print(f'***** {p1_name} WINS *****')
        break
print("That's all folks!")
