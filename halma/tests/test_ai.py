import unittest
import tkinter
import sys
import os
import pytest

from .. import board
from .. import game
from .. import ai

class TestAI(unittest.TestCase):
    def setUp(self):
        self.board = Board(5)
        self.board.red.pos.clear()
        self.board.green.pos.clear()
        self.board.red.pos.add((2,2))
        self.board.green.pos.add((1,3))
        self.ai = AI(self.board)

    def test_optimal(self):
        src, dest = self.ai.get_optimal_move(1, self.board.red.pos, self.board.green.pos, False)
        # assert src == (2,2) and dest == (0,4)
        assert False
