import weapons
import game_functions as gf

class Combatant:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.ac = 0
        self.temp_ac = 0
        self.temp_acmod = 3
        self.spellpoints = 0
        self.run = False
        self.com = ''
        self.initiative = 0
        self.STRmod = 0
        self.DEXmod = 0
        self.INTmod = 0
        self.prof = 2
        self.weapon = 'dagger'
        self.atk_message = 'Roll a d20'
        self.spell_message = ''
        self.action = 1
        self.subtle_action = 1
        self.attack_number = 1
        self.speed = 30
        self.bonus_action = 1

    def roll_initiative(self):
        self.initiative = gf.roll_dice(1, 20) + self.DEXmod

    def reference(self):    # Redefine for spellcasters and players
        print(f'''Player reference:
    Name: {self.name}   HP: {self.hp}   AC: {self.ac}

    Weapon: {self.weapon}

    Modifiers:
        STR: {self.STRmod}  DEX: {self.DEXmod}  INT: {self.INTmod}
    Initiative: {self.initiative}''')

    def command(self):
        self.com = input(f"{self.name}, type a command > ").lower()

    def attack(self, target):   # Redefined for spellcasters
        print(f'{self.name} attacks {target.name}!')
        attack_attempt = False
        atk = 0
        while attack_attempt is False:
            try:
                atk = int(input(f'{self.atk_message} > ')) + self.STRmod + self.prof
                attack_attempt = True
            except ValueError:
                print('Invalid input')
        if atk >= target.ac and atk >= target.temp_ac:
            dmg = self.damage() + self.STRmod
            print(f'{target.name} takes {dmg} damage')
            target.hp -= dmg
            print("Ouch!")
        else:
            print(f'{self.name} missed')

    def defend(self):
        print(f'{self.name} prepares for an incoming attack')
        if self.temp_ac == 0:
            self.temp_ac = self.ac + self.temp_acmod
        else:
            pass

    def equip_weapon(self):
        new_weapon = input("Equip a new weapon > ").lower()
        weapon_set = False
        while weapon_set is False:
            if new_weapon in weapons.list_of_weapons:
                print(f'{self.name} equipped a {new_weapon}!')
                self.weapon = new_weapon
                weapon_set = True
            elif new_weapon == 'remove':
                print(f'{self.name} dropped their weapon!')
                self.weapon = 'none'
                weapon_set = True
            elif new_weapon == 'cancel':
                break
            else:
                print('Invalid weapon')
                new_weapon = input("Equip a new weapon > ").lower()

    def damage(self):   # Needs to be redefined if combatant does not weild a weapon
        dmg = gf.collect_weapon_damage(self.weapon)
        return dmg


class Spellcaster(Combatant):
    def attack(self, target):
        atk = 0
        dmg = 0
        melee_or_spell = input('Melee or spell attack > ')
        m_or_s_attempt = False
        while m_or_s_attempt is False:
            if melee_or_spell == 'melee':
                print(f'{self.name} attacks {target.name}!')
                atk = int(input(f'{self.atk_message} > ')) + self.DEXmod + self.prof
                dmg = self.damage() + self.DEXmod
                m_or_s_attempt = True
            elif melee_or_spell == 'spell':
                dmg = self.cast_spell()
                if dmg == 'cancel':
                    melee_or_spell = input('Melee or spell attack > ')
                else:
                    print(f'{self.name} attacks {target.name} with {self.spell_message}!')
                    atk = int(input(f'{self.atk_message} > ')) + self.INTmod + self.prof
                    m_or_s_attempt = True
            else:
                print('Invalid attack type')
                melee_or_spell = input('Melee or spell attack > ')
        
        if atk >= target.ac and atk >= target.temp_ac:
            print(f'{target.name} takes {dmg} damage')
            target.hp -= dmg
            print("Ouch!")
        else:
            print(f'{self.name} missed')

    def reference(self):
        print(f'''Player reference:
    Name: {self.name}   HP: {self.hp}   AC: {self.ac}   
    
    Spell Points: {self.spellpoints}    Weapon: {self.weapon}
    
    Modifiers:
        STR: {self.STRmod}  DEX: {self.DEXmod}  INT: {self.INTmod}
    Initiative: {self.initiative}''')

    def cast_spell(self):
        dmg = gf.spell_select(self)
        return dmg


class Player(Combatant):
    def set_stats(self, name, hp, ac):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.prof = 0
        self.atk_message = 'Make an attack roll'

    def damage(self):
        dmg = int(input('Roll your damage > '))
        return dmg


class Gnoll(Combatant):
    def set_stats(self, name):
        self.name = name
        self.hp = gf.roll_dice(5, 8)
        self.ac = 15
        self.temp_acmod = 5
        self.STRmod = 2
        self.DEXmod = 1
        self.weapon = 'spear'


class Skeleton(Combatant):
    def set_stats(self, name):
        self.name = name
        self.hp = gf.roll_dice(2, 8) + 4
        self.ac = 13
        self.temp_acmod = 1
        self.STRmod = 0
        self.DEXmod = 2
        self.weapon = 'shortsword'


class Zombie(Combatant):
    def set_stats(self, name):
        self.name = name
        self.hp = gf.roll_dice(3, 8) + 9
        self.ac = 8
        self.temp_acmod = 2
        self.STRmod = 1
        self.DEXmod = -2

    def damage(self):
        dmg = gf.roll_dice(1, 6)
        return dmg


class Acolyte(Spellcaster):
    def set_stats(self, name):
        self.name = name
        self.hp = gf.roll_dice(4, 8) + 8
        self.ac = 12
        self.spellpoints = 5
        self.temp_acmod = 1
        self.STRmod = 0
        self.DEXmod = 1
        self.INTmod = 3
        self.spellmessage = ''
        self.spelloptions = ['fireball', 'frostspike']
