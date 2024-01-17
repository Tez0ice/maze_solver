import unittest

from graphic import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cell(self):
        num_cols = 12
        num_rows = 10
        maze1 = Maze(0,0,num_rows,num_cols,10,10)
        maze2 = Maze(10,10,20,20,10,10)
        maze3 = Maze(20,20,30,30,20,20)
        self.assertEqual(
            len(maze1._cells),
            num_cols,
        )
        self.assertEqual(
            len(maze1._cells[0]),
            num_rows
        )
        self.assertEqual(
            len(maze2._cells),
            20
        )
        self.assertEqual(
            len(maze2._cells[0]),
            20
        )
        self.assertEqual(
            len(maze3._cells),
            30
        )
        self.assertEqual(
            len(maze3._cells),
            30
        )

    def test_top_left_and_bot_right_wall(self):
        num_cols = 12
        num_rows = 10
        maze1 = Maze(0,0,num_rows,num_cols,10,10)
        maze1._break_entrace_and_exit()
        self.assertEqual(
            maze1._cells[0][0]._has_right_wall,
            False
        )
        self.assertEqual(
            maze1._cells[-1][-1]._has_bot_wall,
            False
        )

if __name__ == "__main__":
    unittest.main()