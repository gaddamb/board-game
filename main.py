import numpy as np

from business.move import ObjectMovement


if __name__ == '__main__':
    invalid_table = True
    invalid_pos = True
    play =  True

    while(invalid_table) :
        try:
            print('Please enter \'width\' and \'height\' (ex: 4,4) : ', end='')
            table = input().strip().split(',')
            width = int(table[0])
            height = int(table[1])
            invalid_table = False
        except:
            print('\ninvalid input width or height: ', end='')
            invalid_table = True

    while(invalid_pos) :
        try:
            print('\nPlease enter defualt position of object x,y (ex: 2,2) : ', end='')
            default_pos = input().strip().split(',')
            x = int(default_pos[0])
            y = int(default_pos[1])
            invalid_pos = False
        except:
            print('\ninvalid input x or y')
            invalid_pos = True

    obj = ObjectMovement(width, height, x, y)
    obj.construct_matrix()
    print('''
    0 = quit simulation and print results to ​stdout \n
    1 = move forward one step \n
    2 = move backwards one step \n 
    3 = rotate clockwise 90 degrees (eg north to east) \n
    4 = rotate counterclockwise 90 degrees (eg west to south)''')
    
    obj.print_table_matrix()

    while(play) :
            print('Please enter a number (0-4) for simulation')
            input_by_user = input()
            input_by_user = int(input_by_user)

            try:
                if input_by_user == 1:
                    obj.step_forward()

                elif input_by_user == 2:
                    obj.step_backwards()

                elif input_by_user == 3:
                    obj.rotate_clockwise()

                elif input_by_user == 4:
                    obj.rotate_anti_clockwise()

                if input_by_user == 0:
                    play = False
                else:
                    obj.print_table_matrix()
            except ValueError:            
                print('The object falls off the table: [-1, -1]')

    