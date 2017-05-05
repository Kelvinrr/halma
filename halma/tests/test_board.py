import unittest
import tkinter
import sys
import os
import pytest

from .. import board

Board = board.Board
Team = board.Team

class TestBoard(unittest.TestCase):

    def setUp(self):

        self.board = Board(5)


        self.green_8x8_positions = set({(2, 7), (2, 6), (0, 7), (1, 5), (0, 6),
                       (1, 6), (0, 5), (0, 4), (3, 7), (1, 7)})

        self.red_8x8_positions = set({(7, 3), (7, 0), (7, 1), (6, 1), (6, 0), (6, 2),
                           (5, 0), (5, 1), (7, 2), (4, 0)})

        self.green_10x10_positions = set({(2, 7), (4, 9), (2, 9), (2, 8), (0, 7), (3, 8), (0, 6),
                                        (1, 8), (3, 9), (0, 5), (1, 6), (1, 9), (1, 7), (0, 9),
                                        (0, 8)})

        self.red_10x10_positions = set({(8, 3), (9, 0), (7, 0), (8, 2), (9, 1), (7, 1), (8, 1),
                                        (9, 2), (6, 1), (8, 0), (9, 3), (6, 0), (5, 0), (9, 4),
                                        (7, 2)})

        self.green_16x16_positions = set({(3, 15), (0, 14), (3, 11), (5, 13), (1, 15), (4, 12),
                                          (0, 10), (2, 12), (1, 11), (3, 14), (6, 14), (7, 15),
                                          (0, 15), (1, 14), (4, 13), (0, 11), (2, 13), (1, 10),
                                          (2, 15), (6, 15), (3, 13), (1, 13), (4, 14), (2, 10),
                                          (0, 12), (5, 15), (1, 9), (0, 8), (2, 14), (3, 12),
                                          (1, 12), (4, 15), (2, 11), (0, 13), (5, 14), (0, 9)})

        self.red_16x16_positions = set({(12, 1), (9, 1), (14, 4), (11, 2), (8, 0), (13, 4), (15, 1),
                                        (14, 0), (15, 5), (12, 2), (9, 0), (14, 5), (13, 3), (15, 0),
                                        (14, 1), (11, 1), (15, 4), (10, 0), (12, 3), (13, 2), (15, 3),
                                        (14, 6), (11, 0), (15, 7), (10, 1), (14, 2), (13, 1), (15, 2),
                                        (12, 0), (11, 3), (13, 5), (15, 6), (12, 4), (14, 3), (13, 0),
                                        (10, 2)})
    def test_8x8(self):
        test_board = Board(8)
        assert test_board.green[0] == self.green_8x8_positions
        assert test_board.red[0] == self.red_8x8_positions

    def test_10x10(self):
        test_board = Board(10)
        assert test_board.green[0] == self.green_10x10_positions
        assert test_board.red[0] == self.red_10x10_positions

    def test_16x16(self):
        test_board = Board(16)
        assert test_board.green[0] == self.green_16x16_positions
        assert test_board.red[0] == self.red_16x16_positions

    def test_init(self):
        with self.assertRaises(Exception):
            test_board = Board(2.5)

    def test_wincheck(self):
        test_board = Board(5)
        assert not test_board.winCheck()
        test_board.green = Team(pos = test_board.green.goal, start = test_board.green.start, goal = test_board.green.goal, player = test_board.green.player, goalTile=(0,0))
        print(test_board.winCheck())
        assert test_board.winCheck() == 'g'
        test_board.green = Team(pos = test_board.green.start, start = test_board.green.start, goal = test_board.green.goal, player = test_board.green.player, goalTile=(0,0))
        test_board.red = Team(pos = test_board.red.goal, start = test_board.red.start, goal = test_board.red.goal, player = test_board.red.player, goalTile=(0,0))
        assert test_board.winCheck() == 'r'

    def test_xyToCoord(self):
        assert self.board.xyToCoord(5,4) == "f1"
        with self.assertRaises(Exception):
            self.board.xyToCoord(6,26)
        with self.assertRaises(Exception):
            self.board.xyToCoord(6,-1)
        with self.assertRaises(Exception):
            self.board.xyToCoord(-6,-1)
