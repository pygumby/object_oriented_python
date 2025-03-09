import random


class Monster:
    def __init__(self, n_rows, n_cols, max_speed):
        self.n_rows = n_rows  # Save away
        self.n_cols = n_cols  # Save away
        self.my_row = random.randrange(self.n_rows)  # Chooses a random row
        self.my_col = random.randrange(self.n_cols)  # Chooses a random col
        self.my_speed_x = random.randrange(-max_speed, max_speed + 1)  # Chooses x speed
        self.my_speed_y = random.randrange(-max_speed, max_speed + 1)  # Chooses y speed
        # Set other instance variables like health, power, etc.

    def move(self):
        self.my_row = (self.my_row + self.my_speed_y) % self.n_rows
        self.my_col = (self.my_col + self.my_speed_y) % self.n_cols


N_MONSTERS = 20
N_ROWS = 100  # Could be any size
N_COLS = 200  # Could be any size
MAX_SPEED = 4

monster_list = []  # Start with an empty list

for i in range(N_MONSTERS):
    monster = Monster(N_ROWS, N_COLS, MAX_SPEED)  # Create a Monster
    monster_list.append(monster)  # Add the Monster to our list
