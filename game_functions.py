import random, Monster_SB as msb

# Important game arrays

actions = ['atk', 'cast', 'def', 'run']
subtle_actions = ['equip']

# General dice roller

def roll_dice(num_dice, d_value):
    output = 0
    while num_dice > 0:
        output += random.randint(1, d_value)
        num_dice -= 1
    return output


# Saving throw function

def saving_throw(target, save_type):
    save_attempt = False
    while save_attempt is False:
        if save_type == 'STR':
            try:
                save = int(input(f'{target.save_message} > ')) + target.STR_save_mod
                save_attempt = True
            except ValueError:
                pass
        elif save_type == 'DEX':
            try:
                save = int(input(f'{target.save_message} > ')) + target.DEX_save_mod
                save_attempt = True
            except ValueError:
                pass
        elif save_type == 'CON':
            try:
                save = int(input(f'{target.save_message} > ')) + target.CON_save_mod
                save_attempt = True
            except ValueError:
                pass
        elif save_type == 'INT':
            try:
                save = int(input(f'{target.save_message} > ')) + target.INT_save_mod
                save_attempt = True
            except ValueError:
                pass
        elif save_type == 'WIS':
            try:
                save = int(input(f'{target.save_message} > ')) + target.WIS_save_mod
                save_attempt = True
            except ValueError:
                pass
        elif save_type == 'CHA':
            try:
                save = int(input(f'{target.save_message} > ')) + target.CHA_save_mod
                save_attempt = True
            except ValueError:
                pass
    return save


# Establishes combatant types

def create_player(p_list, p_number):
    combatant_type = input('Combatant type > ').lower()
    p_creation_attempt = False
    while p_creation_attempt is False:
        if combatant_type == 'player':
            p_list[p_number] = msb.Player()
            p_list[p_number].set_stats(input('Name > '), int(input('HP > ')), int(input('AC > ')))
            p_creation_attempt = True
        elif combatant_type == 'gnoll':
            p_list[p_number] = msb.Gnoll()
            p_list[p_number].set_stats(input('Name > '))
            p_creation_attempt = True
        elif combatant_type == 'skeleton':
            p_list[p_number] = msb.Skeleton()
            p_list[p_number].set_stats(input('Name > '))
            p_creation_attempt = True
        elif combatant_type == 'zombie':
            p_list[p_number] = msb.Zombie()
            p_list[p_number].set_stats(input('Name > '))
            p_creation_attempt = True
        elif combatant_type == 'acolyte':
            p_list[p_number] = msb.Acolyte()
            p_list[p_number].set_stats(input('Name > '))
            p_creation_attempt = True
        else:
            print('''
Invalid monster type
            ''')
            combatant_type = input('Monster type > ').lower()
    print(' ')


# Targetting functions

def select_target(range_of_p, p_list):
    target = input('target > ')
    select_attempt = False
    while select_attempt is False:
        for p_number in range_of_p:
            try:
                if target == p_list[p_number].name and p_list[p_number].run is False:
                   target = p_list[p_number]
                else:
                    pass
            except IndexError:
                pass
        if target in p_list:
            select_attempt = True
            break
        elif target == 'help':
            print('''Type a combatants name to target it
Names can be found in "Player Names" list at beginning of Round''')
            target = input('target > ')
        elif target == 'cancel':
            break
        else:
            print('''Invalid target
Type "help" for options''')
            target = input('target > ')
    return target
