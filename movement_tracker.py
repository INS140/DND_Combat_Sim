# This is a test of the possible movement tracker
# If successful this will be implemented into the Combatant class

# It's looking good so far

import game_functions as gf

def map_size():
    print('How large is the map?')
    x_max = gf.player_int_input('Max x value > ')
    y_max = gf.player_int_input('Max y value > ')
    x_range = range(0, x_max)
    y_range = range(0, y_max)
    return [x_range, y_range]


class Test:
    def __init__(self, name):
        self.name = name
        self.movement = 30
        self.coordinate = []
        self.coor_matrix = []

    def start_point(self): # Establishes original starting point
        x = gf.player_int_input(f'Enter starting point for {self.name}: x > ')
        y = gf.player_int_input('y > ')
        coordinate = [x, y]
        self.update_coordinates(coordinate)
        

    def update_coordinates(self, coordinate): # Updates the matrix of points surrounding player
        x, y = coordinate
        self.coordinate = [x, y]
        self.coor_matrix = [[(x - 1), (y + 1)], [x, (y + 1)], [(x + 1), (y + 1)],
                            [(x - 1), y], [x, y], [(x + 1), y],
                            [(x - 1), (y - 1)], [x, (y - 1)], [(x + 1), (y - 1)]]
        print(self.coor_matrix)

    def move(self): 
        x = gf.player_int_input('x movement > ')
        y = gf.player_int_input('y movement > ')
        movement = (abs(x) + abs(y)) * 5
        if movement > self.movement:
            print("That location is too far away")
        else:
            old_x, old_y = self.coordinate
            x += old_x
            y += old_y
            global map_x, map_y
            if x not in map_x or y not in map_y:
                print('That location is out of bounds')
            else:
                new_coordinate = [x, y]
                print(f'{self.name} moves to {new_coordinate}')
                self.update_coordinates(new_coordinate)


if hasattr(Test, 'move'): # useful test here
    print('hooray')

gnoll = Test('gnoll')
skel = Test('skel')
p_list = [gnoll, skel]
map_x, map_y = map_size()

for p in p_list:
    p.start_point()
while True:
    for p in p_list:
        p.move()
        ref_list = p_list.copy()
        ref_list.remove(p)
        for opp in ref_list:
            if p.coordinate in opp.coor_matrix:
                print(f'You are in range of {opp.name}')

    again = input("again > ")
    if again == 'y':
        pass
    else:
        break