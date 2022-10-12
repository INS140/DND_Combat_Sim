from Monster_SB import Combatant

character = False
while character is False:
    try:
        p1 = Combatant(input('Player 1: '), int(input("HP: ")), int(input("AC: ")))
        character = True
    except ValueError:
        print("Invalid value")

character2 = False
while character2 is False:
    try:
        p2 = Combatant(input('Player 2: '), int(input("HP: ")), int(input("AC: ")))
        character2 = True
    except ValueError:
        print("Invalid value")

character3 = False
while character3 is False:
    try:
        p3 = Combatant(input('Player 3: '), int(input("HP: ")), int(input("AC: ")))
        character3 = True
    except ValueError:
        print("Invalid value")


player_list = [p1, p2, p3]
player_com = ''
target = ''
two_chickens = False

print(' ')
print('FIGHT')

while True:
    for player in player_list:
        if player.hp > 0 and player.run is False:
            attempt = False
            player.temp_ac = 0
            print(' ')
            player.command()
            while attempt is False:
                if player.com == 'attack':
                    target = input('target> ')
                    if target == f'{p1.name}':
                        player.attack(p1)
                        attempt = True
                    elif target == f'{p2.name}':
                        player.attack(p2)
                        attempt = True
                    elif target == f'{p3.name}':
                        player.attack(p3)
                        attempt = True
                    else:
                        print('Invalid target')
                        if player is p1:
                            print(f'''
                            Valid targets: "{p2.name}" or "{p3.name}"
                            ''')
                        elif player is p2:
                            print(f'''
                            Valid targets: "{p1.name}" or "{p3.name}"
                            ''')
                        elif player is p3:
                            print(f'''
                            Valid targets: "{p1.name}" or "{p2.name}"
                            ''')
                        else:
                            pass
                elif player.com == 'defend':
                    player.defend()
                    attempt = True
                elif player.com == 'run':
                    print(f'{player.name} chickened out ...')
                    player.run = True
                    attempt = True
                elif player.com == 'help':
                    print('''Options:
    attack - attack a target
    defend - temporarily raise AC
    run - forfeit
                    ''')
                    player.command()
                else:
                    print("Invalid input")
                    print('type "help" for options')
                    player.command()
        if p2.run is True is p3.run:
            print(f'***** {p1.name} WINS *****')
            two_chickens = True
            break
        elif p1.run is True is p3.run:
            print(f'***** {p2.name} WINS *****')
            two_chickens = True
            break
        elif p1.run is True is p2.run:
            print(f'***** {p3.name} WINS *****')
            two_chickens = True
            break
        else:
            pass
    if p1.hp > 0 >= p2.hp and p3.hp <= 0:
        print(f'***** {p1.name} WINS *****')
        break
    elif p2.hp > 0 >= p1.hp and p3.hp <= 0:
        print(f'***** {p2.name} WINS *****')
        break
    elif p3.hp > 0 >= p1.hp and p2.hp <= 0:
        print(f'***** {p3.name} WINS *****')
        break
    elif two_chickens is True:
        break
    else:
        pass
