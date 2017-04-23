import unittest
import tkinter
import sys
import os
import pytest

from .. import board
from .. import game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = game.Halma(5)

    def test_run_command(self):
        assert self.game.run_command("a1->b2") == "Red's Turn"
        assert self.game.run_command("a1->b2") == "Invalid Move"
        
if __name__ == "__main__": # pragma : no cover
        root = Tk()
        size = 5
        game = Halma(size)
        board = game.board
        gui = HalmaGUI(root, game)
        gui.set_board(board)
        root.mainloop()
