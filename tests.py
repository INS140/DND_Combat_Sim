import game_functions as gf, Monster_SB as msb, weapons as wpn, spells as spl

number_of_p = gf.player_int_input('How many players? > ')
range_of_p = range(0, number_of_p)
print('\n')
p_list = gf.create_player(range_of_p)
x = 0
for p in p_list:
    weapon = 'battleaxe'
    p.mh_weapon = gf.assign_weapon(weapon)
    p.mh_weapon.d_value += x
    x += 1

for p in p_list:
    print(f'{p.name} {p.mh_weapon.d_value}')