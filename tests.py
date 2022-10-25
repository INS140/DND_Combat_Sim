import game_functions as gf,Monster_SB as msb

# To shorten variable size, p = player

# Things left to add:
#   timer that keeps track of in combat time
#   player options function
#   adapt spellcasting and attack action
#   combat spells ------ add more
#   multitargeting
#   implement spell descriptions
#   conditions
#   bonus action
#   reactions
#   critcal hits and fails ------ maybe finished, needs more testing
#   Net weapon and special property
#   implement weapon properties ------ In Progress
#   multiattack
#   spell levels and point cost
#   monsters
#   monster special abilities
#   spell slots for monsters
#   replace defend with dodge
#   healing
#   movement counter???
#   noncombat spells
#   passive spell and AoE effects
#   resistance/immunity
#   player stat blocks
#   player levels
#   player/monster inventory
#   class specifics (spell lists, weapon prof, etc)
#   proficiency bonuses
#   saving throws ------ maybe finished, needs more testing
#   player specific actions
#   party/teams
#   django framework

# This section decides how many players there are and their attributes

number_of_p = gf.player_int_input('How many players? > ')

print(' ')
range_of_p = range(0, number_of_p)
p_list = []
for p_number in range_of_p:
    p_list.append(p_number)
    gf.create_player(p_list, p_number)
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
        if player.hp <= 0:
            try:
                p_list_reference_init.remove(player.initiative)
                p_list_reference_name.remove(player.name)
                p_list.remove(player)
            except IndexError:
                pass
            except ValueError:
                pass
            number_of_p -= 1
    if number_of_p == 1:
            break
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
                            result = player.attack(range_of_p, p_list)
                            if result == 'success':
                                action -= 1
                            player.command()
                        elif player.com == 'def':
                            player.defend()
                            action -= 1
                            player.command()
                        elif player.com == 'run':
                            print(f'{player.name} chickened out ...')
                            player.run = True
                            turn_finished = True
                            p_list_reference_init.remove(player.initiative)
                            p_list_reference_name.remove(player.name)
                            number_of_p -= 1
                            print('-' * 100)
                        elif isinstance(player, msb.Spellcaster) is True and player.com == 'cast':
                            result = player.cast_spell(range_of_p, p_list)
                            if result == 'success':
                                action -= 1
                            player.command()
                        elif isinstance(player, msb.Spellcaster) is not True and player.com == 'cast':
                            print("You can't cast spells")
                            player.command()
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
                            print(' ')
                            player.command()
                    else:
                        print("You can't do that")
                        player.command()
                else:
                    if player.com == 'help':
                        print('''Combat Options:
    atk - attack a target
    cast - cast a spell
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
        if number_of_p == 1:
            break

# Decides winner after game ends
for player in p_list:
    if player.hp > 0 and player.run is False:
        print(f'***** {player.name} WINS *****')
        break
    else:
        pass
