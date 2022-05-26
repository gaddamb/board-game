import numpy as np
from config.config import get_config

class ObjectMovement():

    def __init__(self, width, height, x, y) -> None:        
        self.column=int(width)
        self.row=int(height)
        self.pos_x =  int(x)
        self.pos_y = int(y)
        self.standing_direction_of_object = 'N'
        self.play_table_matrix = None
        self.conf = get_config()

    def construct_matrix(self):
        self.play_table_matrix = np.array([[self.conf['CELL'] for _ in range(self.column)] for _ in range(self.row)])

    def step_forward(self):
        self.play_table_matrix[self.pos_x][self.pos_y] = self.conf['CELL']
        if self.standing_direction_of_object == 'N':
            self.pos_y = self.pos_y - 1
        elif self.standing_direction_of_object == 'E':
            self.pos_x = self.pos_x + 1
        elif self.standing_direction_of_object == 'S':
            self.pos_y = self.pos_y + 1
        elif self.standing_direction_of_object == 'W':
            self.pos_x = self.pos_x - 1

    def step_backwards(self):
        self.play_table_matrix[self.pos_x][self.pos_y] = self.conf['CELL']
        if self.standing_direction_of_object == 'N':
            self.pos_y = self.pos_y + 1
        elif self.standing_direction_of_object == 'E':
            self.pos_x = self.pos_x - 1
        elif self.standing_direction_of_object == 'S':
            self.pos_y = self.pos_y - 1
        elif self.standing_direction_of_object == 'W':
            self.pos_x = self.pos_x + 1
            
    def rotate_clockwise(self):
        # move clock wise
        if self.standing_direction_of_object == 'N':
            self.standing_direction_of_object = 'E'
        elif self.standing_direction_of_object == 'E':
            self.standing_direction_of_object = 'S'
        elif self.standing_direction_of_object == 'S':
            self.standing_direction_of_object = 'W'
        elif self.standing_direction_of_object == 'W':
            self.standing_direction_of_object = 'N'

    def rotate_anti_clockwise(self):
        # anti clock wise i.e from west to south
        if self.standing_direction_of_object == 'N':
            self.standing_direction_of_object = 'W'
        elif self.standing_direction_of_object == 'E':
            self.standing_direction_of_object = 'N'
        elif self.standing_direction_of_object == 'S':
            self.standing_direction_of_object = 'E'
        elif self.standing_direction_of_object == 'W':
            self.standing_direction_of_object = 'S'

    def print_table_matrix(self):
        try:            
            self.play_table_matrix[self.pos_x][self.pos_y] = self.conf[self.standing_direction_of_object]
            for arr in self.play_table_matrix.transpose():
                print('')   
                for element in arr:
                    print(element, end='')
            
            print('\nposition is at: ', self.pos_x, self.pos_y)
        except:
            raise ValueError

    def play(self):
        play =  True
        

