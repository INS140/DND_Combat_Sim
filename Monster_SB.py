from time import sleep
import weapons as wpn, spells as spl
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
        self.weapon = wpn.Weapon()
        self.atk_message = 'Roll a d20'
        self.save_message = ''
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
        self.save_message = f'{self.name}, roll a d20'

    def reference(self):    # Redefine for spellcasters and players
        print(f'''Player reference:
    Name: {self.name}   HP: {self.hp}   AC: {self.ac}

    Weapon: {self.weapon.name}

    Modifiers:
        STR: {self.STRmod}  DEX: {self.DEXmod}  INT: {self.INTmod}
    Initiative: {self.initiative}''')

    def command(self):
        self.com = input(f"{self.name}, type a command > ").lower()

    def attack(self, range_of_p, p_list):
        result = ''
        weapon_thrown = False
        target = gf.select_target(range_of_p, p_list)
        if target in p_list:
            if 'finesse' in self.weapon.properties: # STR or DEX
                if self.DEXmod > self.STRmod:
                    mod = self.DEXmod
                else:
                    mod = self.STRmod
            else:
                mod = self.STRmod
            if isinstance(self.weapon, wpn.Ranged) is True: # Ranged weapon attack
                if isinstance(self.weapon, wpn.Dart) is False:
                    mod = self.DEXmod
                d_roll = self.weapon.target_distance()
                if d_roll == 'cancel':
                    result = 'cancel'
                else:
                    if isinstance(self.weapon, wpn.Dart):
                        weapon_thrown = True
            elif self.weapon.thrown is True: # Thrown weapon attack
                throw = input('Throw the weapon (y/n) > ')
                if throw == 'y':
                    d_roll = self.weapon.target_distance()
                    if d_roll == 'cancel':
                        result = 'cancel'
                    else:
                        weapon_thrown = True
                elif throw == 'n':
                    d_roll = gf.player_int_input(gf.roll_message)
                else:
                    print('Invalid input')
            else: # All non-ranged weapons without finesse or thrown
                d_roll = gf.player_int_input(gf.roll_message)
            if result != 'cancel':
                print(f'{self.name} attacks {target.name} with a {self.weapon.name}!')
                sleep(1)
                atk = d_roll + mod + self.prof
                if isinstance(self.weapon, wpn.Unarmed) is True: # Unarmed attack
                    mod = 0
                if d_roll == 1: # Critical failure
                    print('Critical FAIL!')
                    print(f'{self.name} missed horribly')
                elif d_roll == 20: # Critical hit
                    dmg = self.weapon.weapon_critical() + mod
                    print('Critical Hit!')
                    print(f'{target.name} takes {dmg} {self.weapon.dmg_type} damage')
                    target.hp -= dmg
                    print("Ouch!")
                else: # Normal weapon attack
                    if atk >= target.ac and atk >= target.temp_ac: # Attack hit
                        dmg = self.weapon.weapon_damage() + mod
                        print(f'{target.name} takes {dmg} {self.weapon.dmg_type} damage')
                        target.hp -= dmg
                        print("Ouch!")
                    else: # Attack missed
                        print(f'{self.name} missed')
                if target.hp < 1: # Target was killed by attack
                    print(f'{target.name} is dead')
                result = 'success'
        elif target == 'cancel':
            result = 'cancel'
        if weapon_thrown is True: # Removes weapon that has been thrown
            self.weapon = wpn.Unarmed(self.STRmod)
        return result

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
            if new_weapon in wpn.list_of_weapons:
                for weapon in wpn.list_of_weapons_as_objects:
                    if new_weapon == weapon.name:
                        self.weapon = weapon
                        print(f'{self.name} equipped a {new_weapon}!')
                        weapon_set = True
                        break
                    else:
                        pass
            elif new_weapon == 'remove':
                print(f'{self.name} dropped their weapon!')
                self.weapon = wpn.Unarmed(self.STRmod)
                weapon_set = True
            elif new_weapon == 'cancel':
                break
            else:
                print('Invalid weapon')
                new_weapon = input("Equip a new weapon > ").lower()


class Spellcaster(Combatant):
    def __init__(self):
        super().__init__()
        self.spellpoints = 0
        self.casting_mod = 0
        self.spell_save_dc = 8 + self.casting_mod
        self.spell_options = []

    def cast_spell(self, range_of_p, p_list):
        spell_select = input('Which spell would you like to use > ').lower()
        cast_attempt = False
        result = ''
        while cast_attempt is False:
            if spell_select in self.spell_options:
                for sp in spl.spell_list:
                    if spell_select == sp.reference:
                        spell = sp
                        break
                    else:
                        pass
                cast_attempt = True
            elif spell_select == 'cancel':
                result = 'cancel'
                break
            else:
                print("You can't cast that")
                spell_select = input('Which spell would you like to use > ').lower()
        if result == 'cancel':
            pass
        else:
            if isinstance(spell, spl.Attack_spell):
                target = gf.select_target(range_of_p, p_list)
                if target in p_list:
                    print(f'{self.name} attacks {target.name} with {spell.name}!')
                    sleep(1)
                    if spell.roll_type == 'attack':
                        d_roll = gf.player_int_input(gf.roll_message)
                        atk = d_roll + self.casting_mod
                        spell.spell_effect(self, atk, target)
                        result = 'success'
                    elif spell.roll_type == 'save':
                        save = gf.saving_throw(target, spell.save_type)
                        spell.spell_effect(self, save, target)
                        result = 'success'
                    if target.hp < 1:
                        print(f'{target.name} is dead')
                elif target == 'cancel':
                    result = 'cancel'
            else:
                print("You're spell doesn't do damage")
        return result

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
        self.STR_save_mod = 2
        self.DEXmod = 1
        self.DEX_save_mod = 1
        self.weapon = wpn.Spear()


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
        self.DEX_save_mod = 2
        self.weapon = wpn.Shortsword()


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
        self.weapon = wpn.Unarmed(self.STRmod)


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
        self.weapon = wpn.Dagger()
        self.casting_mod = self.INTmod + self.prof
        self.spell_save_dc = 8 + self.casting_mod
        self.spell_options = ['acid splash', 'chill touch']
