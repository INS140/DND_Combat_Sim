import random, Monster_SB as msb, weapons as wpn, copy

# Important game arrays and variables

actions = ['atk', 'cast', 'def', 'run']
subtle_actions = ['equip'] # More will be added later
roll_message = 'Roll a d20 > '
score_to_mod = {1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1, 13: 1, 14: 2, 15: 2, 16: 3, 17: 3,
                18: 4, 19: 4, 20: 5, 21: 5, 22: 6, 23: 6, 24: 7, 25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 30: 10}

monster_dict = {
    'gnoll': msb.Gnoll(),
    'skeleton': msb.Skeleton(),
    'zombie': msb.Zombie(),
    'acolyte': msb.Acolyte()
}
monster_list = monster_dict.keys()

weapons_dict = {'club': wpn.Club(), 'dagger': wpn.Dagger(), 'greatclub': wpn.Greatclub(), 'handaxe': wpn.Handaxe(), 'javelin': wpn.Javelin(),
    'light hammer': wpn.Light_hammer(), 'mace': wpn.Mace(), 'quarterstaff': wpn.Quarterstaff(), 'sickle': wpn.Sickle(), 'spear': wpn.Spear(),
    'light crossbow': wpn.Crossbow_light(), 'dart': wpn.Dart(), 'shortbow': wpn.Shortbow(), 'sling': wpn.Sling(), 'battleaxe': wpn.Battleaxe(),
    'flail': wpn.Flail(), 'glaive': wpn.Glaive(), 'greataxe': wpn.Greataxe(), 'greatsword': wpn.Greatsword(), 'halberd': wpn.Halberd(),
    'lance': wpn.Lance(), 'longsword': wpn.Longsword(), 'maul': wpn. Maul(), 'morningstar': wpn.Morningstar(), 'pike': wpn.Pike(),
    'rapier': wpn.Rapier(), 'scimitar': wpn.Scimitar(), 'shortsword': wpn.Shortsword(), 'trident': wpn.Trident(), 'war pick': wpn.War_pick(),
    'warhammer': wpn.Warhammer(), 'whip': wpn.Whip(), 'blowgun': wpn.Blowgun(), 'hand crossbow': wpn.Crossbow_hand(), 'heavy crossbow': wpn.Crossbow_heavy(),
    'longbow': wpn.Longbow(), 'net': wpn.Net()
}
weapons_list = weapons_dict.keys()

# General dice roller

def roll_dice(num_dice, d_value):
    total = 0
    while num_dice > 0:
        total += random.randint(1, d_value)
        num_dice -= 1
    return total


# Player inputs

def player_int_input(message):
    attempt = False
    while attempt is False:
        try:
            player_input = int(input(message))
            attempt = True
        except ValueError:
            print('Invalid input\n')
    return player_input


# Advantage and Disadvantage

def roll_advantage():
    print('Roll with advantage')
    output = 0
    roll1 = player_int_input(roll_message)
    roll2 = player_int_input(roll_message)
    if roll1 > roll2:
        output = roll1
    else:
        output = roll2
    return output

def roll_disadvantage():
    print('Roll with disadvantage')
    output = 0
    roll1 = player_int_input(roll_message)
    roll2 = player_int_input(roll_message)
    if roll1 < roll2:
        output = roll1
    else:
        output = roll2
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


# Functions for assigning variables to classes

def create_player(range_of_p):
    p_list = []
    for p_number in range_of_p:
        p_list.append(p_number)
        monster_dict_copy = copy.deepcopy(monster_dict)
        while True:
            combatant_type = input('Combatant type > ').lower()
            if combatant_type in monster_list:
                p_list[p_number] = monster_dict_copy.get(combatant_type)
                p_list[p_number].set_stats(input('Name > '))
                print(' ')
                break
            else:
                print('Invalid monster type\n')
    return p_list

def assign_weapon(weapon):
    weapons_dict_copy = copy.deepcopy(weapons_dict)
    weapon = weapons_dict_copy.get(weapon)
    return weapon


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
