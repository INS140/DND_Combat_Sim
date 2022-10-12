import game_functions as gf

# Cantrips

def acid_splash(user):
    dmg = gf.roll_dice(1, 6)
    user.spellmessage = 'Acid Splash'
    return dmg

def chill_touch(user):
    dmg = gf.roll_dice(1, 8)
    user.spellmessage = 'Chill Touch'
    return dmg

def eldritch_blast(user):
    dmg = gf.roll_dice(1, 10)
    user.spellmessage = 'Eldrtich Blast'
    return dmg

def fire_bolt(user):
    dmg = gf.roll_dice(1, 10)
    user.spellmessage = 'Fire Bolt'
    return dmg

def frostbite(user):
    dmg = gf.roll_dice(1, 6)
    user.spellmessage = 'Frostbite'
    return dmg

def poison_spray(user):
    dmg = gf.roll_dice(1, 12)
    user.spellmessage = 'Poison Spray'
    return dmg

def ray_of_frost(user):
    dmg = gf.roll_dice(1, 8)
    user.spellmessage = 'Ray of Frost'
    return dmg

def sacred_flame(user):
    dmg = gf.roll_dice(1, 8)
    user.spellmessage = 'Sacred Flame'
    return dmg

def shocking_grasp(user):
    dmg = gf.roll_dice(1, 8)
    user.spellmessage = 'Shocking Grasp'
    return dmg

def thorn_whip(user):
    dmg = gf.roll_dice(1, 6)
    user.spellmessage = 'Thorn Whip'
    return dmg

def thunderclap(user):
    dmg = gf.roll_dice(1, 6)
    user.spellmessage = 'Thunderclap'
    return dmg

def toll_the_dead(user):
    dmg = gf.roll_dice(1, 8)
    user.spellmessage = 'Toll the Dead'
    return dmg

def vicious_mockery(user):
    dmg = gf.roll_dice(1, 4)
    user.spellmessage = 'Vicious Mockery'
    return dmg

def word_of_radiance(user):
    dmg = gf.roll_dice(1, 6)
    user.spellmessage = 'Word of Radiance'
    return dmg


# 1st level




# Other

def fireball(user):
    dmg = gf.roll_dice(2, 6)
    user.spellpoints -= 2
    user.spellmessage = 'Fireball'
    return dmg

def frostspike(user):
    dmg = gf.roll_dice(2, 8)
    user.spellpoints -= 3
    user.spellmessage = 'Frostspike'
    return dmg

def lightning(user):
    dmg = gf.roll_dice(4, 8)
    user.spellpoints -= 5
    user.spellmessage = 'Lightning'
    return dmg
