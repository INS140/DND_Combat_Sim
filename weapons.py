import game_functions as gf

list_of_weapons = ['club', 'dagger', 'greatclub', 'handaxe', 'javelin', 'light hammer', 'mace', 'quarterstaff', 'sickle',
    'spear', 'light crossbow', 'dart', 'shortbow', 'sling', 'battleaxe', 'flail', 'glaive', 'greataxe', 'greatsword',
    'halberd', 'lance', 'longsword', 'maul', 'morningstar', 'pike', 'rapier', 'scimitar', 'shortsword', 'trident',
    'war pick', 'warhammer', 'whip', 'blowgun', 'hand crossbow', 'heavy crossbow', 'longbow']

# Simple melee weapons

def club():
    damage = gf.roll_dice(1, 4)
    return damage

def dagger():
    damage = gf.roll_dice(1, 4)
    return damage

def greatclub():
    damage = gf.roll_dice(1, 8)
    return damage

def handaxe():
    damage = gf.roll_dice(1, 6)
    return damage

def javelin():
    damage = gf.roll_dice(1, 6)
    return damage

def light_hammer():
    damage = gf.roll_dice(1, 4)
    return damage

def mace():
    damage = gf.roll_dice(1, 6)
    return damage

def quarterstaff():
    damage = gf.roll_dice(1, 6)
    return damage

def sickle():
    damage = gf.roll_dice(1, 4)
    return damage

def spear():
    damage = gf.roll_dice(1, 8)
    return damage


# Simple ranged weapons

def crossbow_light():
    damage = gf.roll_dice(1, 8)
    return damage

def dart():
    damage = gf.roll_dice(1, 4)
    return damage

def shortbow():
    damage = gf.roll_dice(1, 6)
    return damage

def sling():
    damage = gf.roll_dice(1, 4)
    return damage


# Martial melee weapons

def battleaxe():
    damage = gf.roll_dice(1, 8)
    return damage

def flail():
    damage = gf.roll_dice(1, 8)
    return damage

def glaive():
    damage = gf.roll_dice(1, 10)
    return damage

def greataxe():
    damage = gf.roll_dice(1, 12)
    return damage

def greatsword():
    damage = gf.roll_dice(2, 6)
    return damage

def halberd():
    damage = gf.roll_dice(1, 10)
    return damage

def lance():
    damage = gf.roll_dice(1, 12)
    return damage

def longsword():
    damage = gf.roll_dice(1, 8)
    return damage

def maul():
    damage = gf.roll_dice(2, 6)
    return damage

def morningstar():
    damage = gf.roll_dice(1, 8)
    return damage

def pike():
    damage = gf.roll_dice(1, 10)
    return damage

def rapier():
    damage = gf.roll_dice(1, 8)
    return damage

def scimitar():
    damage = gf.roll_dice(1, 6)
    return damage

def shortsword():
    damage = gf.roll_dice(1, 6)
    return damage

def trident():
    damage = gf.roll_dice(1, 6)
    return damage

def war_pick():
    damage = gf.roll_dice(1, 8)
    return damage

def warhammer():
    damage = gf.roll_dice(1, 8)
    return damage

def whip():
    damage = gf.roll_dice(1, 4)
    return damage


# Martial ranged weapons - net, no damage so it's useless atm

def blowgun():
    damage = 1
    return damage

def crossbow_hand():
    damage = gf.roll_dice(1, 6)
    return damage

def crossbow_heavy():
    damage = gf.roll_dice(1, 10)
    return damage

def longbow():
    damage = gf.roll_dice(1, 8)
    return damage
