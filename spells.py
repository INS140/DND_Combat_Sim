import game_functions as gf

# Cantrips

class Spell:
    def __init__(self):
        self.spell_name = ''
        self.type = ''
        self.level = 0
        self.casting_time = ''
        self.range = 0
        self.components = ''
        self.duration = 0
        self.description = ''

    def spell_effect(self):
        pass


class Attack_spell(Spell):
    def __init__(self):
        super().__init__()
        self.num_die = 1
        self.d_value = 6
        self.dmg_type = ''

    def spell_effect(self, user, atk, target):
        if atk >= target.ac and atk >= target.temp_ac:
            dmg = self.spell_damage()
            print(f'{target.name} takes {dmg} {self.dmg_type} damage')
            target.hp -= dmg
            print("Ouch!")
        else:
            print(f'{user.name} missed')

    def spell_damage(self):
        dmg = gf.roll_dice(self.num_die, self.d_value)
        return dmg


class Cantrip(Spell):
    def __init__(self):
        super().__init__()
        self.caster_level = 0


class Acid_splash(Cantrip, Attack_spell):
    def __init__(self):
        super().__init__()
        self.name = 'Acid Splash'
        self.reference = 'acid splash'
        self.type = 'Conjuration'
        self.casting_time = '1 action'
        self.range = 60
        self.components = 'V, S'
        self.dmg_type = 'acid'
        self.description = '''
You hurl a bubble of acid. Choose one or two creatures you can see within
range. If you choose two, they must be within 5 feet of each other. A target
must succeed on a Dexterity saving throw or take 1d6 acid damage.

This spell's damage increases by 1d6 when you reach 5th level (2d6), 11th 
level (3d6), and 17th level (4d6).
        '''


def chill_touch(user):
    dmg = gf.roll_dice(1, 8)
    user.spell_message = 'Chill Touch'
    return dmg

def eldritch_blast(user):
    dmg = gf.roll_dice(1, 10)
    user.spell_message = 'Eldrtich Blast'
    return dmg

def fire_bolt(user):
    dmg = gf.roll_dice(1, 10)
    user.spell_message = 'Fire Bolt'
    return dmg

def frostbite(user):
    dmg = gf.roll_dice(1, 6)
    user.spell_message = 'Frostbite'
    return dmg

def poison_spray(user):
    dmg = gf.roll_dice(1, 12)
    user.spell_message = 'Poison Spray'
    return dmg

def ray_of_frost(user):
    dmg = gf.roll_dice(1, 8)
    user.spell_message = 'Ray of Frost'
    return dmg

def sacred_flame(user):
    dmg = gf.roll_dice(1, 8)
    user.spell_message = 'Sacred Flame'
    return dmg

def shocking_grasp(user):
    dmg = gf.roll_dice(1, 8)
    user.spell_message = 'Shocking Grasp'
    return dmg

def thorn_whip(user):
    dmg = gf.roll_dice(1, 6)
    user.spell_message = 'Thorn Whip'
    return dmg

def thunderclap(user):
    dmg = gf.roll_dice(1, 6)
    user.spell_message = 'Thunderclap'
    return dmg

def toll_the_dead(user):
    dmg = gf.roll_dice(1, 8)
    user.spell_message = 'Toll the Dead'
    return dmg

def vicious_mockery(user):
    dmg = gf.roll_dice(1, 4)
    user.spell_message = 'Vicious Mockery'
    return dmg

def word_of_radiance(user):
    dmg = gf.roll_dice(1, 6)
    user.spell_message = 'Word of Radiance'
    return dmg


# 1st level




# Other

def fireball(user):
    dmg = gf.roll_dice(2, 6)
    user.spellpoints -= 2
    user.spell_message = 'Fireball'
    return dmg

def frostspike(user):
    dmg = gf.roll_dice(2, 8)
    user.spellpoints -= 3
    user.spell_message = 'Frostspike'
    return dmg

def lightning(user):
    dmg = gf.roll_dice(4, 8)
    user.spellpoints -= 5
    user.spell_message = 'Lightning'
    return dmg


# Spell lists

spell_list_as_objects = [Acid_splash()]