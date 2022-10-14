import game_functions as gf

# To shorten variable size, p = player

# Things left to add:
#   add spellcasting action
#   combat spells
#   spell descriptions
#   conditions
#   bonus action
#   critcal hits and fails
#   weapon properties
#   multiattack
#   spell levels and point cost
#   monsters
#   monster special abilities
#   spell slots for monsters
#   add advantage and disadvantage
#   replace defend with dodge
#   healing
#   movement counter???
#   noncombat spells
#   damage types
#   resistance/immunity
#   player stat blocks
#   player levels
#   player/monster inventory
#   class specifics (spell lists, weapon prof, etc)
#   proficiency bonuses
#   saving throws
#   player specific actions
#   party/teams
#   django framework


# This section decides how many players there are and their attributes
p_list_range_create = False
while p_list_range_create is False:
    try:
        number_of_p = int(input('How many players? > '))
        p_list_range_create = True
    except ValueError:
        print('Invalid input')

print(' ')
range_of_p = range(0, number_of_p)
p_list = []
for p_number in range_of_p:
    p_list.append(p_number)
    gf.create_player(p_list, p_number)

# This section is to determine initiative
for player in p_list:
    player.roll_initiative()
    p_list.sort(key=lambda p: p.initiative, reverse=True)

# This creates reference lists for in game use
p_list_reference_init = []
for player in p_list:
    p_list_reference_init.append(player.initiative)
p_list_reference_name = []
for player in p_list:
    p_list_reference_name.append(player.name)

# Intro
print('''

                                    Let the battle
                                        Begin!!!''')
print('-' * 100)
round_num = 0

# This is the actual game
while number_of_p > 1:
    round_num += 1
    for player in p_list:
        if player.hp <= 0 or player.run is True:
            try:
                p_list_reference_init.remove(player.initiative)
                p_list_reference_name.remove(player.name)
            except IndexError:
                pass
            except ValueError:
                pass
    print(f'''
Initiative: {p_list_reference_init}
Player Name: {p_list_reference_name}

Round {round_num}''')
    print('-' * 100)
    for player in p_list:
        if player.hp > 0 and player.run is False:
            player.reference()
            turn_finished = False
            player.temp_ac = 0
            action = player.action
            subtle_action = player.subtle_action
            print(' ')
            player.command()
            while turn_finished is False:
                if player.com in gf.actions:
                    if action != 0:
                        if player.com == 'atk':
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
                                            action -= 1
                                            target = 0
                                        else:
                                            pass
                                    except IndexError:
                                        pass
                                if target == 'help':
                                    print('''Type a combatants name to target it
Names can be found in "Player Names" list at beginning of Round''')
                                    target = input('target > ')
                                elif target == 'cancel':
                                    player.command()
                                    break
                                elif target == 0:
                                    pass
                                else:
                                    print('''Invalid target
Type "help" for options''')
                                    target = input('target > ')
                            if attack_attempt is False:
                                pass
                            elif attack_attempt is True:
                                player.command()
                        elif player.com == 'def':
                            player.defend()
                            action -= 1
                            player.command()
                        elif player.com == 'run':
                            print(f'{player.name} chickened out ...')
                            player.run = True
                            number_of_p -= 1
                            turn_finished = True
                            print('-' * 100)
                    else:
                        print("You have no more actions")
                        player.command()
                elif player.com in gf.subtle_actions:
                    if subtle_action != 0:
                        if player.com == 'equip':
                            weapon = player.weapon
                            player.equip_weapon()
                            if weapon != player.weapon:
                                subtle_action -= 1
                            else:
                                pass
                            print(' ')
                            player.command()
                    else:
                        print("You can't do that")
                        player.command()
                else:
                    if player.com == 'help':
                        print('''Combat Options:
    atk - attack a target
    def - temporarily raise AC
    run - forfeit
    end - end turn
Player Options:
    equip - change weapon
                        ''')
                        player.command()
                    elif player.com == 'end':
                        turn_finished = True
                        print('-' * 100)
                    else:
                        print('''Invalid input"
    Type "help" for options
                        ''')
                        player.command()

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
