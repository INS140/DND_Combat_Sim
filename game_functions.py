import random, Monster_SB, spells, weapons

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


# Weapon selection and damage output

def collect_weapon_damage(weapon):
    if weapon == 'club':
        dmg = weapons.club()
    elif weapon == 'dagger':
        dmg = weapons.dagger()
    elif weapon == 'greatclub':
        dmg = weapons.greatclub()
    elif weapon == 'handaxe':
        dmg = weapons.handaxe()
    elif weapon == 'javelin':
        dmg = weapons.javelin()
    elif weapon == 'light hammer':
        dmg = weapons.light_hammer()
    elif weapon == 'mace':
        dmg = weapons.mace()
    elif weapon == 'quarterstaff':
        dmg = weapons.quarterstaff()
    elif weapon == 'sickle':
        dmg = weapons.sickle()
    elif weapon == 'spear':
        dmg = weapons.spear()
    elif weapon == 'light crossbow':
        dmg = weapons.crossbow_light()
    elif weapon == 'dart':
        dmg = weapons.dart()
    elif weapon == 'shortbow':
        dmg = weapons.shortbow()
    elif weapon == 'sling':
        dmg = weapons.sling()
    elif weapon == 'battleaxe':
        dmg = weapons.battleaxe()
    elif weapon == 'flail':
        dmg = weapons.flail()
    elif weapon == 'glaive':
        dmg = weapons.glaive()
    elif weapon == 'greataxe':
        dmg = weapons.greataxe()
    elif weapon == 'greatsword':
        dmg = weapons.greatsword()
    elif weapon == 'halberd':
        dmg = weapons.halberd()
    elif weapon == 'lance':
        dmg = weapons.lance()
    elif weapon == 'longsword':
        dmg = weapons.longsword()
    elif weapon == 'maul':
        dmg = weapons.maul()
    elif weapon == 'morningstar':
        dmg = weapons.morningstar()
    elif weapon == 'pike':
        dmg = weapons.pike()
    elif weapon == 'rapier':
        dmg = weapons.rapier()
    elif weapon == 'scimitar':
        dmg = weapons.scimitar()
    elif weapon == 'shortsword':
        dmg = weapons.shortsword()
    elif weapon == 'trident':
        dmg = weapons.trident()
    elif weapon == 'war pick':
        dmg = weapons.war_pick()
    elif weapon == 'warhammer':
        dmg = weapons.warhammer()
    elif weapon == 'whip':
        dmg = weapons.whip()
    elif weapon == 'blowgun':
        dmg = weapons.blowgun()
    elif weapon == 'hand crossbow':
        dmg = weapons.crossbow_hand()
    elif weapon == 'heavy crossbow':
        dmg = weapons.crossbow_heavy()
    elif weapon == 'longbow':
        dmg = weapons.longbow()
    else:
        dmg = 0
    return dmg


# Spell selection for spellcasters

# Determines if user can cast the given spell
def spell_select(user):
    spell = input('Which spell would you like to use > ').lower()
    cast_attempt = False
    while cast_attempt is False:
        if spell == 'cancel':
            dmg = 'cancel'
            cast_attempt = True
        else:
            if spell in user.spelloptions:
                dmg = collect_spell_damage(user, spell)
                if dmg == 'invalid':
                    spell = input('Which spell would you like to use > ').lower()
                else:
                    cast_attempt = True
            else:
                print("You can't cast that spell")
                spell = input('Which spell would you like to use > ').lower()
    return dmg

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
