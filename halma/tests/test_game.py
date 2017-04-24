import unittest
import tkinter
import sys
import os
import pytest

from .. import board
from .. import game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = game.Halma(5, 10, 'r')

    def test_run_command(self):
        assert self.game.run_command("a1->b2") == "Red's Turn"
        assert self.game.run_command("a1->b2") == "Invalid Move"
