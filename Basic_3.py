from Monster_SB import Combatant

# To shorten variable size, p = player

# This section decides how many players there are and their attributes
number_of_p = int(input('How many players? > '))
range_of_p = range(0, number_of_p)
p_list = []
for p_number in range_of_p:
    p_list += [f'{p_number}']
    p_list[p_number] = Combatant(input(f'Player {p_number + 1} > '), 10, 5)

# This section is to determine initiative
for player in p_list:
    player.roll_initiative()
    p_list.sort(key=lambda p: p.initiative, reverse=True)


# This is the actual game
while number_of_p > 1:
    for player in p_list:
        if player.hp > 0 and player.run is False:
            turn_finished = False
            player.temp_ac = 0
            print(' ')
            player.command()
            while turn_finished is False:
                if player.com == 'attack':
                    target = input('target > ')
                    attack_attempt = False
                    while attack_attempt is False:
                        for p_number in range_of_p:
                            try:
                                if target == p_list[p_number].name and p_list[p_number].run is False:
                                    player.attack(p_list[p_number])
                                    if p_list[p_number].hp <= 0:
                                        print(f'{p_list[p_number].name} is dead')
                                        number_of_p -= 1
                                    attack_attempt = True
                                else:
                                    pass
                            except IndexError:
                                pass
                        if attack_attempt is False:
                            print('Invalid target')
                            target = input('target > ')
                        else:
                            pass
                    turn_finished = True
                    print('-' * 100)
                elif player.com == 'defend':
                    player.defend()
                    turn_finished = True
                    print('-' * 100)
                elif player.com == 'run':
                    print(f'{player.name} chickened out ...')
                    player.run = True
                    number_of_p -= 1
                    turn_finished = True
                    print('-' * 100)
                elif player.com == 'help':
                    print('''Options:
    attack - attack a target
    defend - temporarily raise AC
    run - forfeit
                    ''')
                    player.command()
                elif player.com == 'pass':
                    turn_finished = True
                    print('-' * 100)
                else:
                    print("Invalid input")
                    print('type "help" for options')
                    player.command()
        elif player.hp <= 0:
            pass

        if number_of_p <= 1:
            break
        else:
            pass

# Decides winner after game ends
for player in p_list:
    if player.hp > 0 and player.run is False:
        print(f'***** {player.name} WINS *****')
        break
    else:
        pass
