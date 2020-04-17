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
        self.grid = None
        print('hello tomrrow')

    def ask_difficulty(self):
        #update the difficulty attribute based on input
        difficulty_mapping = {'e': 'easy', 'm': 'medium', 'h': 'hard'}
        difficulty_input = ''
        while difficulty_input not in difficulty_mapping:
            difficulty_input = input('Select difficulty (e for easy, m for medium, h for hard) : ')
        self.difficulty = difficulty_mapping[difficulty_input]

    def create_grid(self):
        #create grid with parameters based on difficulty
        if self.difficulty == 'easy':
            self.grid = Grid(4,4,2)
        elif self.difficulty == 'medium':
            self.grid = Grid(6,6,5)
        else:
            self.grid = Grid(8,8,15)

    def compute_exit_point(self):
        #compute exit point of the laser beam
        self.exit_point = self.grid.laser_beam.find_exit_point(self.grid)

    def print_grid(self):
        #prints the grid with laser beam entry point
        grid_state = self.grid.state
        laser_init_pos = self.grid.laser_beam.init_pos
        laser_init_dir = self.grid.laser_beam.init_direction

        direction_str = ''
        if laser_init_dir[0] == 1 and laser_init_dir[1] == 0:
            direction_str = 'v'
        elif laser_init_dir[0] == -1 and laser_init_dir[1] == 0:
            direction_str = '^'
        elif laser_init_dir[0] == 0 and laser_init_dir[1] == 1:
            direction_str = '>'
        elif laser_init_dir[0] == 0 and laser_init_dir[1] == -1:
            direction_str = '<'
        else:
            raise ValueError(f'Not an acceptable direction : {laser_init_dir}')
        grid_state[laser_init_pos[0]][laser_init_pos[1]] = direction_str

        for line in grid_state:
            print('  '.join(line))
            print()

    def ask_guess(self):
        #update the player_guess attribute based on input
        self.player_guess = input('What is the exit point of the laser beam ? ')


    def player_guess_to_coords(self):
        #use the string.split(',') method and string slicing to get coords
        self.player_guess.replace(' ', '')
        if '(' in self.player_guess:
            self.player_guess = self.player_guess[1:-1]
        try:
            guess_x, guess_y = self.player_guess.split(',')
        except:
            print('Wrong guess format.')
        return (int(guess_x), int(guess_y))


    def print_result(self):
        #prints message depending on if the game is won or not
        guess_coords = self.player_guess_to_coords()
        if (self.exit_point == guess_coords).all():
            print('Victory')
        else:
            print(f'You lose. You should have said {self.exit_point}')


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
        #you can use a double loop to get the list of all coordinates
        #and the np.choice to choose n INDEXES in the list

        possible_coordinates = [(i, j) for i in range(self.W) for j in range(self.H)]
        i_mirrors_pos = np.random.choice(range(self.W * self.H), self.nb_mirrors)
        mirrors_pos = [possible_coordinates[i] for i in i_mirrors_pos]

        grid_state = [[' ' for i in range(self.W)] for j in range(self.H)]
        for mirror_pos in mirrors_pos:
            mirror_str = np.random.choice(['\\', '/'])
            grid_state[mirror_pos[0]][mirror_pos[1]] = mirror_str
        augmented_grid_state = [[str(i) for i in range(self.W+2)]]
        for i in range(self.H):
            line = grid_state[i]
            augmented_grid_state += [[str(i + 1)] + line[:] + [str(i + 1)]]
        augmented_grid_state += [[str(self.H+1)] + [str(i) for i in range(1, self.W+1)] + [str(self.H+1)]]
        self.state = augmented_grid_state

    def init_laser_beam(self):
        #initialize laser beam attributes
        side = np.random.choice(['up', 'down', 'right', 'left'])
        if side in ['up', 'down']:
            ini_x = 0 if side=='up' else self.H+1
            ini_y = np.random.randint(1, self.W)
            dir = np.array([1,0]) if side=='up' else np.array([-1,0])
        else:
            ini_x = np.random.randint(1, self.H)
            ini_y = 0 if side=='left' else self.W+1
            dir = np.array([0,1]) if side=='left' else np.array([0,-1])
        self.laser_beam = LaserBeam(ini_x, ini_y, dir)

class LaserBeam:
    def __init__(self, initial_x, initial_y, ini_dir):
        self.init_pos = np.array([initial_x, initial_y])
        self.init_direction = ini_dir

    def is_in_grid(self, pos, W, H):
        #returns True if pos is in grid
        return 1<=pos[0]<=H and 1<=pos[1]<=W

    def move(self, prev_pos, prev_dir, grid):
        #moves the laser beam for one step and returns (pos, dir, state ('moving' or 'stopping')) tuple
        current_pos = prev_pos + prev_dir
        if not self.is_in_grid(current_pos, grid.W, grid.H):
            return current_pos, prev_dir, 'stopping'
        cell_content = grid.state[current_pos[0]][current_pos[1]]
        dir = np.copy(prev_dir)
        if cell_content == '/':
            dir = np.array([-dir[1], dir[0]])
        elif cell_content == '\\':
            dir = np.array([dir[1], dir[0]])
        return current_pos, dir, 'moving'

    def find_exit_point(self, grid):
        #finds the exit point of the laser beam
        current_pos, current_dir, state = \
            self.move(self.init_pos, self.init_direction, grid)
        while state == 'moving':
            current_pos, current_dir, state = \
                self.move(current_pos, current_dir, grid)
        return current_pos

if __name__ == '__main__':
    game = Game()
    game.ask_difficulty()
    game.create_grid()
    game.compute_exit_point()
    game.print_grid()
    game.ask_guess()
    game.print_result()
