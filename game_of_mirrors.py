'''
This is a skeleton for the Game of mirror exercise. To run the script, open a Terminal / Command Prompt,
navigate to the directory that contains this file and run 'python game_of_mirrors.py'
'''

import numpy as np

class Game:
    def __init__(self):
        self.difficulty = ''
        self.player_guess = ''
        self.exit_point = (0,0)
        self.grid = None #A Grid object

    def ask_difficulty(self):
        #update the difficulty attribute based on input

    def create_grid(self):
        #create grid with parameters based on difficulty

    def compute_exit_point(self):
        #compute exit point of the laser beam

    def print_grid(self):
        #prints the grid with laser beam entry point

    def ask_guess(self):
        #update the player_guess attribute based on input

    def player_guess_to_coords(self):
        #use the string.split(',') method and string slicing to get coords

    def print_result(self):
        #prints message depending on if the game is won or not


class Grid:
    def __init__(self, W, H, nb_mirrors):
        '''
        This allows you to create a grid this way : G = Grid(5,5,3)
        '''
        self.W = W
        self.H = H
        self.nb_mirrors = nb_mirrors
        self.laser_beam = '' ### A LaserBeam object
        self.state = [] #state[2][2] -> content of the cell on position (2,2)
        self.random_build()
        self.init_laser_beam()

    def random_build(self):
        #Builds the grid with random mirror position and shape
        #you can use this syntax :
        # my_list = [<something> for i in ... for j in ...] to get the list of all coordinates
        # and the np.choice function to choose n INDEXES in the list.
        # Then select the elements corresponding to these indexes

    def init_laser_beam(self):
        #initialize laser beam attributes

class LaserBeam:
    def __init__(self, initial_x, initial_y, ini_dir):
        self.init_pos = None #define with initial_x and initial_y
        self.init_direction = None #define with ini_dir

    def is_in_grid(self, pos, W, H):
        #returns True if pos is in grid

    def move(self, prev_pos, prev_dir, grid):
        #moves the laser beam for one step and returns (pos, dir, state) tuple
        # where state is 'moving' or 'stopping'

    def find_exit_point(self, grid):
        #finds the exit point of the laser beam using the move function

if __name__ == '__main__':
    game = Game()
    game.ask_difficulty()
    game.create_grid()
    game.compute_exit_point()
    game.print_grid()
    game.ask_guess()
    game.print_result()
