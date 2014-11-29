from random import randrange

class GameOfLife():
    map = []

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def initialize_map(self):
        self.map = []
        for y in range(0, self.height):
            tmp_map = []
            for x in range(0, self.width):
                tmp_map.append(0)
            self.map.append(tmp_map)

    def spawn(self, y, x):
        self.map[y][x] = 1

    def get_map(self):
        return self.map

    def initialize_game(self, number_of_lifes):
        while number_of_lifes > 0:
            position = [randrange(self.height), randrange(self.width)]
            if self.map[position[0]][position[1]] < 1:
                self.map[position[0]][position[1]] = 1

                number_of_lifes -= 1

    def next_frame(self):
        next_map = []
        for y in range(0, self.height):
            next_map_line = []
            for x in range(0, self.width):
                neighboor_count = self.count_neighboors(y, x)
                if neighboor_count < 2 or neighboor_count > 3:
                    next_map_line.append(0)
                elif neighboor_count == 3:
                    next_map_line.append(1)
                else:
                    next_map_line.append(self.map[y][x])
            next_map.append(next_map_line)

        self.map = next_map


    def count_neighboors(self, y, x):
        number_of_neighboors = 0
        for y_offset in range(-1, 2):
            for x_offset in range(-1, 2):
                new_x = x + x_offset
                new_y = y + y_offset
                if 0 <= new_y < self.height \
                        and 0 <= new_x < self.width \
                        and self.map[new_y][new_x] > 0 \
                        and (new_x != x or new_y != y):
                    number_of_neighboors += 1

        return number_of_neighboors