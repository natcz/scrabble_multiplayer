import unittest
from Board import *
from CheckBoard import *
from Letters import *
from Hint import *


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board = Board(3)

    def testBoardupdate(self):
        board_proper = Board(3)
        board_proper.board = [['_', 'A', '_'],
                              ['_', 'L', '_'],
                              ['_', 'E', '_']]
        coords = [(0, 1), (1, 1), (2, 1)]
        self.board.boardUpdate('ale', coords)
        self.assertEqual(board_proper.board, self.board.board)


class CheckBoardTest(unittest.TestCase):

    def setUp(self):
        self.board = Board(3)
        l = Letters()
        self.eng_dict = l.makeDict()
        self.checkB = CheckBoard(self.board.board)

    def testCheckBoard(self):
        coords1 = [(0, 1), (1, 1), (2, 1)]
        coords2 = [(0, 0)]
        self.assertTrue(self.checkB.checkBoard(self.eng_dict,
                                               'AND',
                                               coords1))
        self.assertFalse(self.checkB.checkBoard(self.eng_dict,
                                                'X',
                                                coords2))


class HintTest(unittest.TestCase):

    def setUp(self):
        self.board = Board(5)
        self.board.board = [['_', 'A', '_', 'E', '_'],
                            ['_', 'L', '_', 'E', '_'],
                            ['_', 'E', '_', '_', '_'],
                            ['_', 'E', '_', '_', '_'],
                            ['_', 'E', '_', '_', '_']]
        l = Letters()
        self.eng_dict = l.makeDict()
        self.rack = []
        self.hint = Hint(self.board.board, self.eng_dict, self.rack)

    def testFree(self):
        self.assertEqual(self.hint.freeUp(3, 1), 0)
        self.assertNotEqual(self.hint.freeUp(3, 3), 3)

        self.assertEqual(self.hint.freeDown(3, 1), 0)
        self.assertEqual(self.hint.freeDown(1, 3), 3)
        self.assertNotEqual(self.hint.freeDown(1, 3), 0)

        self.assertEqual(self.hint.freeLeft(1, 3), 1)
        self.assertNotEqual(self.hint.freeLeft(1, 3), 2)

        self.assertNotEqual(self.hint.freeRight(1, 3), 3)
        self.assertEqual(self.hint.freeRight(1, 3), 1)

if __name__ == "__main__":
    unittest.main()
