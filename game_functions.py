import random, Monster_SB, spells, weapons

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


# Establishes combatant types

def create_player(p_list, p_number):
    combatant_type = input('Combatant type > ').lower()
    p_creation_attempt = False
    while p_creation_attempt is False:
        if combatant_type == 'player':
            p_list[p_number] = Monster_SB.Player()
            p_list[p_number].set_stats(input('Name > '), int(input('HP > ')), int(input('AC > ')))
            p_creation_attempt = True
        elif combatant_type == 'gnoll':
            p_list[p_number] = Monster_SB.Gnoll()
            p_list[p_number].set_stats(input('Name > '))
            p_creation_attempt = True
        elif combatant_type == 'skeleton':
            p_list[p_number] = Monster_SB.Skeleton()
            p_list[p_number].set_stats(input('Name > '))
            p_creation_attempt = True
        elif combatant_type == 'zombie':
            p_list[p_number] = Monster_SB.Zombie()
            p_list[p_number].set_stats(input('Name > '))
            p_creation_attempt = True
        elif combatant_type == 'acolyte':
            p_list[p_number] = Monster_SB.Acolyte()
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


# Collects the spell and determines damage
def collect_spell_damage(user, spell):
    spell_select_attempt = False
    not_enough = False
    invalid = False
    while spell_select_attempt is False:
        if spell == 'acid splash':
            dmg = spells.acid_splash(user)
            spell_select_attempt = True
        elif spell == 'chill touch':
            dmg = spells.chill_touch(user)
            spell_select_attempt = True
        elif spell == 'eldritch blast':
            dmg = spells.eldritch_blast(user)
            spell_select_attempt = True
        elif spell == 'fire_bolt':
            dmg = spells.fire_bolt(user)
            spell_select_attempt = True
        elif spell == 'frostbite':
            dmg = spells.frostbite(user)
            spell_select_attempt = True
        elif spell == 'poison spray':
            dmg = spells.poison_spray(user)
            spell_select_attempt = True
        elif spell == 'ray of frost':
            dmg = spells.ray_of_frost(user)
            spell_select_attempt = True
        elif spell == 'sacred flame':
            dmg = spells.sacred_flame(user)
            spell_select_attempt = True
        elif spell == 'shocking grasp':
            dmg = spells.shocking_grasp(user)
            spell_select_attempt = True
        elif spell == 'thorn whip':
            dmg = spells.thorn_whip(user)
            spell_select_attempt = True
        elif spell == 'fireball':
            if user.spellpoints >= 2:
                dmg = spells.fireball(user)
                spell_select_attempt = True
            else:
                print("Not enough spell points")
                not_enough = True
                break
        elif spell == 'frostspike':
            if user.spellpoints >= 3:
                dmg = spells.frostspike(user)
                spell_select_attempt = True
            else:
                print("Not enough spell points")
                not_enough = True
                break
        elif spell == 'lightning':
            if user.spellpoints >= 5:
                dmg = spells.lightning(user)
                spell_select_attempt = True
            else:
                print("Not enough spell points")
                not_enough = True
                break
        elif spell == 'cancel':
            dmg = 'cancel'
            break
        else:
            print('Invalid spell')
            invalid = True
    if not_enough is True or invalid is True:
        dmg = 'invalid'
    else:
        pass
    return dmg
