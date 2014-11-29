import unittest
from gameoflife.gameoflife import GameOfLife


class GameOfLifeTest(unittest.TestCase):
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

    # Count neighboors
    def test_count_neightboors_with_four_in_the_middle(self):
        # Four neighboors in the middle
        self.game_of_life.spawn(5, 5)
        self.game_of_life.spawn(5, 4)
        self.game_of_life.spawn(5, 6)
        self.game_of_life.spawn(4, 5)
        self.game_of_life.spawn(6, 5)

        self.assertEquals(self.game_of_life.count_neighboors(5, 5), 4)

    def test_count_neightboors_with_two_at_the_bottom_left(self):
        # Two neighboors at the bottom left
        self.game_of_life.spawn(9, 9)
        self.game_of_life.spawn(8, 9)
        self.game_of_life.spawn(9, 8)

        self.assertEquals(self.game_of_life.count_neighboors(9, 9), 2)

    def test_count_neightboors_with_three_at_the_top_right(self):
         # Three neighboors at the top right
        self.game_of_life.spawn(0, 0)
        self.game_of_life.spawn(0, 1)
        self.game_of_life.spawn(1, 0)
        self.game_of_life.spawn(1, 1)

        self.assertEquals(self.game_of_life.count_neighboors(0, 0), 3)

    def test_underpopulation_no_neighboor(self):
        # No neighboor
        self.game_of_life.spawn(5, 5)
        self.game_of_life.next_frame()

        map = self.game_of_life.get_map()
        self.assertEquals(map[5][5], 0)

    # Underpopulation
    def test_underpopulation_one_neighboor(self):
        # One neighboor
        self.game_of_life.spawn(6, 5)
        self.game_of_life.next_frame()

        map = self.game_of_life.get_map()
        self.assertEquals(map[5][5], 0)

    # Overpopulation
    def test_overpopulation(self):
        # Four neighboors
        self.game_of_life.spawn(5, 5)
        self.game_of_life.spawn(5, 4)
        self.game_of_life.spawn(5, 6)
        self.game_of_life.spawn(4, 5)
        self.game_of_life.spawn(6, 5)

        self.game_of_life.next_frame()

        map = self.game_of_life.get_map()
        self.assertEquals(map[5][5], 0)

    # Survival
    def test_survival_two_neighboors(self):
        # Two neighboors
        self.game_of_life.spawn(5, 5)
        self.game_of_life.spawn(5, 6)
        self.game_of_life.spawn(6, 5)

        self.game_of_life.next_frame()

        map = self.game_of_life.get_map()
        self.assertEquals(map[5][5], 1)

    def test_survival_three_neighboors(self):
        # Three neighboors
        self.game_of_life.spawn(5, 5)
        self.game_of_life.spawn(5, 6)
        self.game_of_life.spawn(6, 5)
        self.game_of_life.spawn(4, 5)

        self.game_of_life.next_frame()

        map = self.game_of_life.get_map()
        self.assertEquals(map[5][5], 1)

    # Birth
    def test_birth(self):
        # Three neighboors
        self.game_of_life.spawn(5, 6)
        self.game_of_life.spawn(6, 5)
        self.game_of_life.spawn(4, 5)

        self.game_of_life.next_frame()

        map = self.game_of_life.get_map()
        self.assertEquals(map[5][5], 1)

if __name__ == '__main__':
    unittest.main()
