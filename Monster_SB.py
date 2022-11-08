from time import sleep
import weapons as wpn, spells as spl, game_functions as gf

class Combatant:
    def __init__(self):
        self.type = ''
        self.name = ''
        self.hp = 0
        self.hp_max = 0
        self.hp_num_die = 0
        self.hp_d_value = 8
        self.hpmod = 0
        self.ac = 0
        self.temp_ac = 0
        self.temp_acmod = 3
        self.sp = 0
        self.run = False
        self.com = ''
        self.initiative = 0
        self.STRmod = 0
        self.DEXmod = 0
        self.CONmod = 0
        self.INTmod = 0
        self.WISmod = 0
        self.CHAmod = 0
        self.prof = 2
        self.mh_weapon = wpn.Unarmed(self.STRmod)
        self.oh_weapon = wpn.Unarmed(self.STRmod)
        self.two_handed_weapon = False
        self.save_message = ''
        self.spell_message = ''
        self.action = 1
        self.subtle_action = 1
        self.attack_number = 1
        self.speed = 30
        self.bonus_action = 1

    def set_stats(self, name):
        self.name = name
        self.hp_max = self.hp = gf.roll_dice(self.hp_num_die, self.hp_d_value) + self.hpmod
        self.initiative = gf.roll_dice(1, 20) + self.DEXmod
        self.save_message = f'{self.name}, roll a d20'

    def reference(self):    # Redefine for spellcasters and players
        print(f'''Player reference:
    Name: {self.name}  | HP: Max: {self.hp_max} Current: {self.hp}  | AC: {self.ac}  | Initiative: {self.initiative}
    ___________________________________________________________
      STR: {self.STRmod}  | DEX: {self.DEXmod}  | CON: {self.CONmod}  | INT: {self.INTmod}  | WIS: {self.WISmod}  | CHA: {self.CHAmod}
    ___________________________________________________________
    Weapons: {self.mh_weapon.name}, {self.oh_weapon.name}''')

    def command(self):
        self.com = input(f"{self.name}, type a command > ").lower()

    def attack(self, range_of_p, p_list):
        result = ''
        weapon_thrown = False
        target = gf.select_target(range_of_p, p_list)
        if target in p_list:
            if 'finesse' in self.mh_weapon.properties: # STR or DEX
                if self.DEXmod > self.STRmod:
                    mod = self.DEXmod
                else:
                    mod = self.STRmod
            else:
                mod = self.STRmod
            if isinstance(self.mh_weapon, wpn.Ranged) is True: # Ranged weapon attack
                if isinstance(self.mh_weapon, wpn.Dart) is False:
                    mod = self.DEXmod
                d_roll = self.mh_weapon.target_distance()
                if d_roll == 'cancel':
                    result = 'cancel'
                else:
                    if isinstance(self.mh_weapon, wpn.Dart):
                        weapon_thrown = True
            elif self.mh_weapon.thrown is True: # Thrown weapon attack
                throw = input('Throw the weapon (y/n) > ')
                if throw == 'y':
                    d_roll = self.mh_weapon.target_distance()
                    if d_roll == 'cancel':
                        result = 'cancel'
                    else:
                        weapon_thrown = True
                else:
                    d_roll = gf.player_int_input(gf.roll_message)
            else: # All non-ranged weapons without finesse or thrown
                d_roll = gf.player_int_input(gf.roll_message)
            if result != 'cancel':
                print(f'{self.name} attacks {target.name} with a {self.mh_weapon.name}!')
                sleep(1)
                atk = d_roll + mod + self.prof
                if isinstance(self.mh_weapon, wpn.Unarmed) is True: # Unarmed attack
                    mod = 0
                if d_roll == 1: # Critical failure
                    print('Critical FAIL!')
                    print(f'{self.name} missed horribly')
                elif d_roll == 20: # Critical hit
                    dmg = self.mh_weapon.weapon_critical() + mod
                    print('Critical Hit!')
                    print(f'{target.name} takes {dmg} {self.mh_weapon.dmg_type} damage')
                    target.hp -= dmg
                    print("Ouch!")
                else: # Normal weapon attack
                    if atk >= target.ac and atk >= target.temp_ac: # Attack hit
                        dmg = self.mh_weapon.weapon_damage() + mod
                        print(f'{target.name} takes {dmg} {self.mh_weapon.dmg_type} damage')
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
            self.mh_weapon = wpn.Unarmed(self.STRmod)
        return result

    def defend(self):
        print(f'{self.name} prepares for an incoming attack')
        if self.temp_ac == 0:
            self.temp_ac = self.ac + self.temp_acmod
        else:
            pass

    def equip_weapon(self):
        weapon_set = False
        vers_two_hand = False
        while weapon_set is False:
            new_weapon = input("Equip/remove a weapon > ").lower()
            if new_weapon in gf.weapons_list:
                new_weapon = gf.assign_weapon(new_weapon)
                if isinstance(self.mh_weapon, wpn.Unarmed):
                    equip_mh = False
                    if 'versatile' in new_weapon.properties: # Needs testing
                        while True:
                            one_or_two = input('One or two hands > ').lower()
                            if one_or_two == 'one' or one_or_two == '1':
                                self.mh_weapon = new_weapon
                                equip_mh = True
                                break
                            elif one_or_two == 'two' or one_or_two == '2':
                                vers_two_hand = True
                                break
                            else:
                                print('Invalid input')
                    if 'two-handed' in new_weapon.properties or vers_two_hand is True: # Needs testing
                        if isinstance(self.oh_weapon, wpn.Unarmed):
                            self.mh_weapon = self.oh_weapon = new_weapon
                            self.two_handed_weapon = True
                            equip_mh = True
                        else:
                            print(f"You can't equip a two-handed weapon with a {self.oh_weapon.name} equipped in off-hand")
                    else:
                        self.mh_weapon = new_weapon
                        equip_mh = True
                    if vers_two_hand is True and equip_mh is True: # Needs testing/change
                        self.mh_weapon.d_value += 2
                        self.two_handed_weapon = True
                    if equip_mh is True:
                        print(f'{self.name} equipped a {new_weapon.name} to main-hand!')
                elif isinstance(self.oh_weapon, wpn.Unarmed):
                    equip_oh = False
                    if 'two-handed' in new_weapon.properties:
                        print("You can't equip a two-handed weapon with a weapon equipped in main-hand")
                    else:
                        self.oh_weapon = new_weapon
                        equip_oh = True
                    if equip_oh is True:
                        print(f'{self.name} equipped a {new_weapon.name} to off-hand!')
                else:
                    print("You can't equip a weapon with both hands full")
                weapon_set = True
                break
            elif new_weapon == 'shield': # develop later
                pass
            elif new_weapon == 'remove':
                remove = False
                if self.two_handed_weapon is True:
                    self.mh_weapon = self.oh_weapon = wpn.Unarmed(self.STRmod)
                    self.two_handed_weapon = False
                    remove = True
                else:
                    while True:
                        main_or_off = input('Main-hand or off-hand (main/off)> ').lower()
                        if main_or_off == 'main' and isinstance(self.mh_weapon, wpn.Unarmed) is False:
                            self.mh_weapon = wpn.Unarmed(self.STRmod)
                            remove = True
                            break
                        elif main_or_off == 'main' and isinstance(self.mh_weapon, wpn.Unarmed) is True:
                            print('You have no weapon euipped in that hand')
                        elif main_or_off == 'off' and isinstance(self.oh_weapon, wpn.Unarmed) is False:
                            self.oh_weapon = wpn.Unarmed(self.STRmod)
                            remove = True
                            break
                        elif main_or_off == 'off' and isinstance(self.oh_weapon, wpn.Unarmed) is True:
                            print('You have no weapon euipped in that hand')
                        elif main_or_off == 'cancel':
                            break
                        else:
                            print('Invalid input')
                            print("Enter 'cancel' to quit")
                if remove is True:
                    print(f'{self.name} sheathed their weapon!')
                    weapon_set = True
            elif new_weapon == 'cancel':
                break
            else:
                print('Invalid weapon')

    def orient_weapon(self): # Needs to be developed
        pass

    def set_player_attributes(self):
        output = ''
        while True:
            attribute_select = input('Which attribute would you like to change > ')
            if attribute_select == 'name':
                    self.name = input('Enter new name > ')
                    self.save_message = f'{self.name}, roll a d20'
            elif attribute_select == 'ac':
                self.ac = gf.player_int_input('Enter new AC > ')
            elif attribute_select == 'hp':
                self.hp = gf.player_int_input('Enter new HP > ')
            elif attribute_select == 'sp':
                self.sp = gf.player_int_input('Enter new SP > ')
            elif attribute_select == 'speed':
                self.speed = gf.player_int_input('Enter new speed > ')
            elif attribute_select == 'prof':
                self.prof = gf.player_int_input('Enter new proficiency bonus > ')
            elif attribute_select == 'init':
                print('WARNING: This will not take effect until the next Round') # Still buggy, but better
                cont = input('Continue (y/n) > ')
                if cont == 'y':
                    self.initiative = gf.player_int_input('Enter new initiative > ')
                    output = 'init change'
                else:
                    pass
            elif attribute_select == 'str':
                score = gf.player_int_input('Enter new STR score > ')
                mod = gf.score_to_mod.get(score)
                self.STRmod = mod
            elif attribute_select == 'dex':
                score = gf.player_int_input('Enter new DEX score > ')
                mod = gf.score_to_mod.get(score)
                self.DEXmod = mod
            elif attribute_select == 'con':
                score = gf.player_int_input('Enter new CON score > ')
                mod = gf.score_to_mod.get(score)
                self.CONmod = mod
            elif attribute_select == 'int':
                score = gf.player_int_input('Enter new INT score > ')
                mod = gf.score_to_mod.get(score)
                self.INTmod = mod
            elif attribute_select == 'wis':
                score = gf.player_int_input('Enter new WIS score > ')
                mod = gf.score_to_mod.get(score)
                self.WISmod = mod
            elif attribute_select == 'cha':
                score = gf.player_int_input('Enter new CHA score > ')
                mod = gf.score_to_mod.get(score)
                self.CHAmod = mod
            elif attribute_select == 'help':
                print('''Attribute options:
    name - Change player name
    ac - Change player AC
    hp - Chnage player HP
    sp - Change player SP
    init - Change player initiative
    speed - Change player base speed
    prof - Change player proficiency bonus
    str - Change Strength score
    dex - Change Dexterity score
    con - Change Constitution score
    int - Chnage Intellect score
    wis - Change Wisdom score
    cha - Change Charisma score
    ''')
            else:
                print('Invalid input')
            self.reference()
            again = input('Change another attribute (y/n)> ').lower()
            if again == 'y':
                pass
            else:
                break
        return output

    def options(self, action):
        print('''Options:
    equip - Equip or remove a weapon
    orient - Change which hand(s) you are holding a weapon with
    set - Change player attributes
    exit - Leave player options
    ''')
        output = ''
        while True:
            option_select = input('Choose option > ').lower()
            if option_select in gf.subtle_actions:
                if action != 0 and option_select == 'equip':
                    weapon_mh = self.mh_weapon
                    weapon_oh = self.oh_weapon
                    self.equip_weapon()
                    if weapon_mh != self.mh_weapon or weapon_oh != self.oh_weapon:
                        output = 'subtle used'
                        break
                else:
                    print("You can't equip any more weapons")
            elif option_select == 'orient':
                self.orient_weapon()
            elif 'set' in option_select:
                result = self.set_player_attributes()
                if result == 'init change':
                    output = 'init change'
                    break
            elif option_select == 'exit':
                break
            else:
                print('Invalid input')
        return output


class Spellcaster(Combatant):
    def __init__(self):
        super().__init__()
        self.sp = 0
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
    Name: {self.name}  | HP: {self.hp}  | AC: {self.ac}  | Initiative: {self.initiative}
    Spell Points: {self.sp}
    ___________________________________________________________
      STR: {self.STRmod}  | DEX: {self.DEXmod}  | CON: {self.CONmod}  | INT: {self.INTmod}  | WIS: {self.WISmod}  | CHA: {self.CHAmod}
    ___________________________________________________________
    Weapons: {self.mh_weapon.name}, {self.oh_weapon.name}''')



class Player(Combatant): # Needs to be updated, DO NOT USE AS IS
    def set_stats(self, name, hp, ac):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.prof = 0

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
        self.mh_weapon = wpn.Spear()
        self.oh_weapon = wpn.Shield()


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
        self.mh_weapon = wpn.Shortsword()
        self.oh_weapon = wpn.Unarmed(self.STRmod)


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
        self.mh_weapon = wpn.Unarmed(self.STRmod)
        self.oh_weapon = wpn.Unarmed(self.STRmod)


class Acolyte(Spellcaster):
    def __init__(self):
        super().__init__()
        self.type = 'acolyte'
        self.hp_num_die = 4
        self.hpmod = 8
        self.ac = 12
        self.sp = 5
        self.temp_acmod = 1
        self.STRmod = 0
        self.DEXmod = 1
        self.INTmod = 3
        self.mh_weapon = wpn.Dagger()
        self.casting_mod = self.INTmod + self.prof
        self.spell_save_dc = 8 + self.casting_mod
        self.spell_options = ['acid splash', 'chill touch']
