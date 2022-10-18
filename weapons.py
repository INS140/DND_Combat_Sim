import game_functions as gf


class Weapon:
    def __init__(self):
        self.name = ''
        self.num_die = 1
        self.d_value = 6
        self.dmg_type = 'piercing'

    def weapon_damage(self):
        dmg = gf.roll_dice(self.num_die, self.d_value)
        return dmg

# Simple melee weapons

class Club(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'club'
        self.d_value = 4
        self.dmg_type = 'bludgeoning'

class Dagger(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'dagger'
        self.d_value = 4

class Greatclub(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'greatclub'
        self.d_value = 8
        self.dmg_type = 'bludgeoning'

class Handaxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'handaxe'
        self.dmg_type = 'slashing'

class Javelin(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'javelin'

class Light_hammer(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'light hammer'
        self.d_value = 4
        self.dmg_type = 'bludgeoning'

class Mace(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'mace'
        self.dmg_type = 'bludgeoning'

class Quarterstaff(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'quarterstaff'
        self.dmg_type = 'bludgeoning'

class Sickle(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'sickle'
        self.d_value = 4
        self.dmg_type = 'slashing'

class Spear(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'spear'

# Simple ranged weapons

class Crossbow_light(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'light crossbow'
        self.d_value = 8

class Dart(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'dart'
        self.d_value = 4

class Shortbow(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'shortbow'

class Sling(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'sling'
        self.d_value = 4
        self.dmg_type = 'bludgeoning'

# Martial melee weapons

class Battleaxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'battleaxe'
        self.d_value = 8
        self.dmg_type = 'slashing'

class Flail(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'flail'
        self.d_value = 8
        self.dmg_type = 'bludgeoning'

class Glaive(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'glaive'
        self.d_value = 10
        self.dmg_type = 'slashing'

class Greataxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'greataxe'
        self.d_value = 12
        self.dmg_type = 'slashing'

class Greatsword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'greatsword'
        self.num_die = 2
        self.dmg_type = 'slashing'

class Halberd(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'halberd'
        self.d_value = 10
        self.dmg_type = 'slashing'

class Lance(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'lance'
        self.d_value = 12

class Longsword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'longsword'
        self.d_value = 8
        self.dmg_type = 'slashing'

class Maul(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'maul'
        self.num_die = 2
        self.dmg_type = 'bludgeoning'

class Morningstar(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'morningstar'
        self.d_value = 8
        self.dmg_type = 'bludgeoning'
class Pike(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'pike'
        self.d_value = 10

class Rapier(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'rapier'
        self.d_value = 8

class Scimitar(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'scimitar'
        self.dmg_type = 'slashing'

class Shortsword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'shortsword'
        self.dmg_type = 'slashing'

class Trident(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'trident'

class War_pick(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'war pick'
        self.d_value = 8

class Warhammer(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'warhammer'
        self.d_value = 8
        self.dmg_type = 'bludgeoning'

class Whip(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'whip'
        self.d_value = 4
        self.dmg_type = 'slashing'

# Martial ranged weapons - net, no damage so it's useless atm

class Blowgun(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'blowgun'
        self.d_value = 1

class Crossbow_hand(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'hand crossbow'

class Crossbow_heavy(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'heavy crossbow'
        self.d_value = 10

class Longbow(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'longbow'
        self.d_value = 8


# Unarmed and speical weapons

class Unarmed(Weapon):
    def __init__(self):
        super().__init__()
        self.dmg_type = 'bludgeoning'


list_of_weapons = ['club', 'dagger', 'greatclub', 'handaxe', 'javelin', 'light hammer', 'mace', 'quarterstaff', 'sickle',
    'spear', 'light crossbow', 'dart', 'shortbow', 'sling', 'battleaxe', 'flail', 'glaive', 'greataxe', 'greatsword',
    'halberd', 'lance', 'longsword', 'maul', 'morningstar', 'pike', 'rapier', 'scimitar', 'shortsword', 'trident',
    'war pick', 'warhammer', 'whip', 'blowgun', 'hand crossbow', 'heavy crossbow', 'longbow']


list_of_weapons_as_objects = [Club(), Dagger(), Greatclub(), Handaxe(), Javelin(), Light_hammer(), Mace(), Quarterstaff(), Sickle(), Spear(), Crossbow_light(),
    Dart(), Shortbow(), Sling(), Battleaxe(), Flail(), Glaive(), Greataxe(), Greatsword(), Halberd(), Lance(), Longsword(), Maul(), Morningstar(), Pike(), Rapier(),
    Scimitar(), Shortsword(), Trident(), War_pick(), Warhammer(), Whip(), Blowgun(), Crossbow_hand(), Crossbow_heavy(), Longbow(), Unarmed()]