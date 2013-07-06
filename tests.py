import unittest
from game import GameBoard
from validator import Validator
from exceptions import NotYourTurn
from exceptions import InvalidMove


class ChessTest(unittest.TestCase):
    def test_input_format(self):
        board = GameBoard()
        with self.assertRaises(InvalidMove):
            board.move_current_figure(1, 0, 3, 0)
            board.move_current_figure(6, 0, 5, 0)
            board.move_current_figure(0, 1, 2, 0)
            board.move_current_figure(6, 3, 5, 2)

    def test_knight_move(self):
        board = GameBoard()
        with self.assertRaises(InvalidMove):
            board.move_current_figure(1, 1, 2, 1)
            board.move_current_figure(7, 1, 5, 0)
            board.move_current_figure(0, 1, 2, 2)
            board.move_current_figure(5, 0, 5, 2)

    def test_rock_move(self):
        board = GameBoard()
        with self.assertRaises(InvalidMove):
            board.move_current_figure(1, 0, 3, 0)
            board.move_current_figure(6, 0, 4, 0)
            board.move_current_figure(0, 0, 2, 0)
            board.move_current_figure(7, 0, 5, 0)
            board.move_current_figure(2, 0, 3, 4)

    def test_bishop_move(self):
        board = GameBoard()
        with self.assertRaises(InvalidMove):
            board.move_current_figure(1, 3, 3, 3)
            board.move_current_figure(6, 2, 5, 2)
            board.move_current_figure(0, 2, 3, 5)
            board.move_current_figure(7, 2, 3, 5)
            board.move_current_figure(3, 5, 3, 3)

    def test_queen_move(self):
        board = GameBoard()
        with self.assertRaises(InvalidMove):
            board.move_current_figure(1, 3, 3, 3)
            board.move_current_figure(6, 3, 4, 3)
            board.move_current_figure(0, 3, 2, 3)
            board.move_current_figure(7, 3, 5, 3)
            board.move_current_figure(2, 3, 3, 5)

    def test_king_move(self):
        board = GameBoard()
        with self.assertRaises(InvalidMove):
            board.move_current_figure(1, 4, 3, 4)
            board.move_current_figure(6, 1, 5, 1)
            board.move_current_figure(0, 4, 1, 4)
            board.move_current_figure(6, 3, 6, 3)
            board.move_current_figure(1, 4, 3, 4)

    def test_pawn_move(self):
        board = GameBoard()
        with self.assertRaises(InvalidMove):
            board.move_current_figure(1, 0, 3, 0)
            board.move_current_figure(6, 4, 5, 4)
            board.move_current_figure(3, 0, 3, 1)

    def test_next_turn(self):
        board = GameBoard()
        board.move_current_figure(1, 0, 2, 0)
        self.assertEqual('Next turn', board.get_status())
        board.move_current_figure(6, 0, 5, 0)
        self.assertEqual('Next turn', board.get_status())

    def test_check_turn(self):
        board = GameBoard()
        with self.assertRaises(NotYourTurn):
            board.move_current_figure(1, 1, 3, 1)
            board.move_current_figure(1, 3, 3, 3)

    def test_check_chess(self):
        board = GameBoard()
        board.move_current_figure(1, 4, 3, 4)
        board.move_current_figure(6, 5, 4, 5)
        board.move_current_figure(0, 3, 4, 7)
        self.assertEqual('Chess', board.get_status())

if __name__ == '__main__':
    unittest.main()
