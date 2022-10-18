import weapons, spells
import game_functions as gf

class Combatant:
    def __init__(self):
        self.type = ''
        self.name = ''
        self.hp = 0
        self.hp_num_die = 0
        self.hp_d_value = 8
        self.hpmod = 0
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
        self.weapon = weapons.Weapon()
        self.atk_message = 'Roll a d20'
        self.spell_message = ''
        self.action = 1
        self.subtle_action = 1
        self.attack_number = 1
        self.speed = 30
        self.bonus_action = 1

    def set_stats(self, name):
        self.name = name
        self.hp = gf.roll_dice(self.hp_num_die, self.hp_d_value) + self.hpmod
        self.initiative = gf.roll_dice(1, 20) + self.DEXmod

    def reference(self):    # Redefine for spellcasters and players
        print(f'''Player reference:
    Name: {self.name}   HP: {self.hp}   AC: {self.ac}

    Weapon: {self.weapon.name}

    Modifiers:
        STR: {self.STRmod}  DEX: {self.DEXmod}  INT: {self.INTmod}
    Initiative: {self.initiative}''')

    def command(self):
        self.com = input(f"{self.name}, type a command > ").lower()

    def attack(self, target):
        print(f'{self.name} attacks {target.name} with a {self.weapon.name}!')
        attack_attempt = False
        while attack_attempt is False:
            try:
                atk = int(input(f'{self.atk_message} > ')) + self.STRmod + self.prof
                attack_attempt = True
            except ValueError:
                print('Invalid input')
        if atk >= target.ac and atk >= target.temp_ac:
            dmg = self.weapon.weapon_damage() + self.STRmod
            print(f'{target.name} takes {dmg} {self.weapon.dmg_type} damage')
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
                for wpn in weapons.list_of_weapons_as_objects:
                    if new_weapon == wpn.name:
                        self.weapon = wpn
                        print(f'{self.name} equipped a {new_weapon}!')
                        weapon_set = True
                        break
                    else:
                        pass
            elif new_weapon == 'remove':
                print(f'{self.name} dropped their weapon!')
                self.weapon = None
                weapon_set = True
            elif new_weapon == 'cancel':
                break
            else:
                print('Invalid weapon')
                new_weapon = input("Equip a new weapon > ").lower()


class Spellcaster(Combatant):
    def __init__(self):
        super().__init__()
        self.casting_mod = 0
        self.spell_options = []

    def cast_spell(self):
        spell_select = input('Which spell would you like to use > ').lower()
        cast_attempt = False
        while cast_attempt is False:
            if spell_select in self.spell_options:
                for sp in spells.spell_list_as_objects:
                    if spell_select == sp.reference:
                        spell = sp
                        break
                    else:
                        pass
                cast_attempt = True
            elif spell_select == 'cancel':
                spell = 'cancel'
                break
            else:
                print("You can't cast that")
                spell_select = input('Which spell would you like to use > ').lower()
        return spell
                

    def reference(self):
        print(f'''Player reference:
    Name: {self.name}   HP: {self.hp}   AC: {self.ac}   
    
    Spell Points: {self.spellpoints}    Weapon: {self.weapon.name}
    
    Modifiers:
        STR: {self.STRmod}  DEX: {self.DEXmod}  INT: {self.INTmod}
    Initiative: {self.initiative}''')



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
    def __init__(self):
        super().__init__()
        self.type = 'gnoll'
        self.hp_num_die = 5
        self.ac = 15
        self.temp_acmod = 5
        self.STRmod = 2
        self.DEXmod = 1
        self.weapon = weapons.Spear()


class Skeleton(Combatant):
    def __init__(self):
        super().__init__()
        self.type = 'skeleton'
        self.hp_num_die = 2
        self.hpmod = 4
        self.ac = 13
        self.temp_acmod = 1
        self.STRmod = 0
        self.DEXmod = 2
        self.weapon = weapons.Shortsword()


class Zombie(Combatant):
    def __init__(self):
        super().__init__()
        self.type = 'zombie'
        self.hp_num_die = 3
        self.hpmod = 9
        self.ac = 8
        self.temp_acmod = 2
        self.STRmod = 1
        self.DEXmod = -2
        self.weapon = weapons.Unarmed()


class Acolyte(Spellcaster):
    def __init__(self):
        super().__init__()
        self.type = 'acolyte'
        self.hp_num_die = 4
        self.hpmod = 8
        self.ac = 12
        self.spellpoints = 5
        self.temp_acmod = 1
        self.STRmod = 0
        self.DEXmod = 1
        self.INTmod = 3
        self.weapon = weapons.Dagger()
        self.casting_mod = self.INTmod + self.prof
        self.spellmessage = ''
        self.spell_options = ['fireball', 'frostspike', 'acid splash']
