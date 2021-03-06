import unittest
from gameoflife.gameoflife import GameOfLife

class TestGameOfLife(unittest.TestCase):
    def setUp(self):
        self.game_of_life = GameOfLife(10, 10)
        self.game_of_life.initialize_map()

    def tearDown(self):
        del self.game_of_life

    # Initialize map
    def test_initialize_map(self):
        self.game_of_life.initialize_map()

        map = self.game_of_life.get_map()
        self.assertEquals(len(map), 10)
        self.assertEquals(len(map[0]), 10)

    # Spawning
    def test_spawn(self):
        self.game_of_life.spawn(5, 5)

        map = self.game_of_life.get_map()
        self.assertEquals(map[5][5], 1)

    # Initialize game
    def test_initialize_game(self):
        self.game_of_life.initialize_game(5)

        counter = 0
        map = self.game_of_life.get_map()
        for y in range(0, len(map)):
            for x in range(0, len(map[y])):
                if map[y][x] > 0:
                    counter += 1

        self.assertEquals(counter, 5)

    # Count neighbors
    def test_count_neightboors_with_four_in_the_middle(self):
        # Four neighbors in the middle
        self.game_of_life.spawn(5, 5)
        self.spawn_neighboors(5, 5, 4)

        self.assertEquals(self.game_of_life.count_neighbors(5, 5), 4)

    def test_count_neightboors_with_two_at_the_bottom_left(self):
        # Two neighbors at the bottom left
        self.game_of_life.spawn(9, 9)
        self.spawn_neighboors(9, 9, 2)

        self.assertEquals(self.game_of_life.count_neighbors(9, 9), 2)

    def test_count_neightboors_with_three_at_the_top_right(self):
         # Three neighbors at the top right
        self.game_of_life.spawn(0, 0)
        self.spawn_neighboors(0, 0, 3)

        self.assertEquals(self.game_of_life.count_neighbors(0, 0), 3)

    def test_underpopulation_no_neighbor(self):
        # No neighbor
        self.game_of_life.spawn(5, 5)
        self.game_of_life.next_frame()

        map = self.game_of_life.get_map()
        self.assertEquals(map[5][5], 0)

    # Underpopulation
    def test_underpopulation_one_neighbor(self):
        # One neighbor
        self.game_of_life.spawn(5, 5)
        self.spawn_neighboors(5, 5, 1)
        self.game_of_life.next_frame()

        map = self.game_of_life.get_map()
        self.assertEquals(map[5][5], 0)

    # Overpopulation
    def test_overpopulation(self):
        # Four neighbors
        self.game_of_life.spawn(5, 5)
        self.spawn_neighboors(5, 5, 4)

        self.game_of_life.next_frame()

        map = self.game_of_life.get_map()
        self.assertEquals(map[5][5], 0)

    # Survival
    def test_survival_two_neighbors(self):
        # Two neighbors
        self.game_of_life.spawn(5, 5)
        self.spawn_neighboors(5, 5, 2)

        self.game_of_life.next_frame()

        map = self.game_of_life.get_map()
        self.assertEquals(map[5][5], 1)

    def test_survival_three_neighbors(self):
        # Three neighbors
        self.game_of_life.spawn(5, 5)
        self.spawn_neighboors(5, 5, 3)

        self.game_of_life.next_frame()

        map = self.game_of_life.get_map()
        self.assertEquals(map[5][5], 1)

    # Birth
    def test_birth(self):
        # Three neighbors
        self.spawn_neighboors(5, 5, 3)

        self.game_of_life.next_frame()

        map = self.game_of_life.get_map()
        self.assertEquals(map[5][5], 1)

    def spawn_neighboors(self, x, y, amount):
        counter = 0
        map = self.game_of_life.get_map()
        for y_offset in range(-1, 2):
            for x_offset in range(-1, 2):
                new_x = x + x_offset
                new_y = y + y_offset
                if 0 <= new_y < len(map) \
                        and 0 <= new_x < len(map[y]) \
                        and (new_x != x or new_y != y):
                    self.game_of_life.spawn(new_y, new_x)

                    counter += 1
                    if counter >= amount :
                        return

if __name__ == '__main__':
    unittest.main()
