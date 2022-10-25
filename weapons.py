import game_functions as gf


class Weapon:
    def __init__(self):
        self.name = ''
        self.num_die = 1
        self.d_value = 6
        self.dmg_type = 'piercing'
        self.normal_range = 0
        self.long_range = 0
        self.thrown = False
        self.properties = []

    def weapon_damage(self):
        dmg = gf.roll_dice(self.num_die, self.d_value)
        return dmg

    def weapon_critical(self):
        num_die = self.num_die * 2
        dmg = gf.roll_dice(num_die, self.d_value)
        return dmg

    def target_distance(self):
        target_distance = gf.player_int_input('How far is the target > ')
        if self.normal_range >= target_distance > 5:
            d_roll = gf.player_int_input(gf.roll_message)
        elif self.long_range >= target_distance > self.normal_range:
            d_roll = gf.roll_disadvantage()
        else:
            print("You can't attack that target")
            d_roll = 'cancel'
        return d_roll

# Weapon attack types

class Melee(Weapon):
    def __init__(self):
        super().__init__()
        self.normal_range = 20
        self.long_range = 60


class Ranged(Weapon):
    def __init__(self):
        super().__init__()
        self.normal_range = 80
        self.long_range = 320


# Simple melee weapons

class Club(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'club'
        self.d_value = 4
        self.dmg_type = 'bludgeoning'
        self.properties = ['light']

class Dagger(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'dagger'
        self.d_value = 4
        self.thrown = True
        self.properties = ['finesse', 'light']

class Greatclub(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'greatclub'
        self.d_value = 8
        self.dmg_type = 'bludgeoning'
        self.properties = ['two-handed']

class Handaxe(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'handaxe'
        self.dmg_type = 'slashing'
        self.thrown = True
        self.properties =['light']

class Javelin(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'javelin'
        self.thrown = True
        self.normal_range = 30
        self.long_range = 120

class Light_hammer(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'light hammer'
        self.d_value = 4
        self.dmg_type = 'bludgeoning'
        self.thrown = True
        self.properties = ['light']

class Mace(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'mace'
        self.dmg_type = 'bludgeoning'

class Quarterstaff(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'quarterstaff'
        self.dmg_type = 'bludgeoning'
        self.properties = ['versatile']

class Sickle(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'sickle'
        self.d_value = 4
        self.dmg_type = 'slashing'
        self.properties = ['light']

class Spear(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'spear'
        self.thrown = True
        self.properties = ['versatile']


# Simple ranged weapons

class Crossbow_light(Ranged):
    def __init__(self):
        super().__init__()
        self.name = 'light crossbow'
        self.d_value = 8
        self.properties = ['loading', 'two-handed']


class Dart(Ranged):
    def __init__(self):
        super().__init__()
        self.name = 'dart'
        self.d_value = 4
        self.thrown = True
        self.normal_range = 20
        self.long_range = 60
        self.properties = ['finesse']

class Shortbow(Ranged):
    def __init__(self):
        super().__init__()
        self.name = 'shortbow'
        self.properties = ['two-handed']

class Sling(Ranged):
    def __init__(self):
        super().__init__()
        self.name = 'sling'
        self.d_value = 4
        self.dmg_type = 'bludgeoning'
        self.normal_range = 30
        self.long_range = 120


# Martial melee weapons

class Battleaxe(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'battleaxe'
        self.d_value = 8
        self.dmg_type = 'slashing'
        self.properties = ['versatile']

class Flail(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'flail'
        self.d_value = 8
        self.dmg_type = 'bludgeoning'

class Glaive(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'glaive'
        self.d_value = 10
        self.dmg_type = 'slashing'
        self.properties = ['heavy', 'reach', 'two-handed']

class Greataxe(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'greataxe'
        self.d_value = 12
        self.dmg_type = 'slashing'
        self.properties = ['heavy', 'two-handed']

class Greatsword(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'greatsword'
        self.num_die = 2
        self.dmg_type = 'slashing'
        self.properties = ['heavy', 'two-handed']

class Halberd(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'halberd'
        self.d_value = 10
        self.dmg_type = 'slashing'
        self.properties = ['heavy', 'reach', 'two-handed']

class Lance(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'lance'
        self.d_value = 12
        self.properties = ['reach', 'special']

class Longsword(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'longsword'
        self.d_value = 8
        self.dmg_type = 'slashing'
        self.properties = ['versatile']

class Maul(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'maul'
        self.num_die = 2
        self.dmg_type = 'bludgeoning'
        self.properties = ['heavy', 'two-handed']

class Morningstar(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'morningstar'
        self.d_value = 8
        self.dmg_type = 'bludgeoning'

class Pike(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'pike'
        self.d_value = 10
        self.properties = ['heavy', 'reach', 'two-handed']

class Rapier(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'rapier'
        self.d_value = 8
        self.properties = ['finesse']

class Scimitar(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'scimitar'
        self.dmg_type = 'slashing'
        self.properties = ['finesse', 'light']

class Shortsword(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'shortsword'
        self.dmg_type = 'slashing'
        self.properties = ['finesse', 'light']

class Trident(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'trident'
        self.thrown = True
        self.properties = ['versatile']

class War_pick(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'war pick'
        self.d_value = 8

class Warhammer(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'warhammer'
        self.d_value = 8
        self.dmg_type = 'bludgeoning'
        self.properties = ['versatile']

class Whip(Melee):
    def __init__(self):
        super().__init__()
        self.name = 'whip'
        self.d_value = 4
        self.dmg_type = 'slashing'
        self.properties = ['finesse', 'reach']

# Martial ranged weapons - net, no damage so it's useless atm

class Blowgun(Ranged):
    def __init__(self):
        super().__init__()
        self.name = 'blowgun'
        self.d_value = 1
        self.normal_range = 25
        self.long_range = 100
        self.properties = ['loading']

class Crossbow_hand(Ranged):
    def __init__(self):
        super().__init__()
        self.name = 'hand crossbow'
        self.normal_range = 30
        self.long_range = 120
        self.properties = ['light', 'loading']

class Crossbow_heavy(Ranged):
    def __init__(self):
        super().__init__()
        self.name = 'heavy crossbow'
        self.d_value = 10
        self.normal_range = 100
        self.long_range = 400
        self.properties = ['heavy', 'loading', 'two-handed']

class Longbow(Ranged):
    def __init__(self):
        super().__init__()
        self.name = 'longbow'
        self.d_value = 8
        self.normal_range = 150
        self.long_range = 600
        self.properties = ['heavy', 'two-handed']


# Unarmed and special weapons

class Unarmed(Melee):
    def __init__(self, mod):
        super().__init__()
        self.dmg = mod
        self.dmg_type = 'bludgeoning'

    def weapon_damage(self):
        if self.dmg > 1:
            dmg = self.dmg
        else:
            dmg = 1
        return dmg

    def weapon_critical(self):
        if self.dmg > 1:
            dmg = self.dmg
        else:
            dmg = 1
        dmg *= 2
        return dmg

# Important weapon lists

list_of_weapons = ['club', 'dagger', 'greatclub', 'handaxe', 'javelin', 'light hammer', 'mace', 'quarterstaff', 'sickle',
    'spear', 'light crossbow', 'dart', 'shortbow', 'sling', 'battleaxe', 'flail', 'glaive', 'greataxe', 'greatsword',
    'halberd', 'lance', 'longsword', 'maul', 'morningstar', 'pike', 'rapier', 'scimitar', 'shortsword', 'trident',
    'war pick', 'warhammer', 'whip', 'blowgun', 'hand crossbow', 'heavy crossbow', 'longbow']


list_of_weapons_as_objects = [Club(), Dagger(), Greatclub(), Handaxe(), Javelin(), Light_hammer(), Mace(), Quarterstaff(), Sickle(), Spear(), Crossbow_light(),
    Dart(), Shortbow(), Sling(), Battleaxe(), Flail(), Glaive(), Greataxe(), Greatsword(), Halberd(), Lance(), Longsword(), Maul(), Morningstar(), Pike(), Rapier(),
    Scimitar(), Shortsword(), Trident(), War_pick(), Warhammer(), Whip(), Blowgun(), Crossbow_hand(), Crossbow_heavy(), Longbow()]