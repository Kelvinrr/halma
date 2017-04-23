import unittest
import tkinter
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath('..'))

from .. import game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = game.Halma(5)

    def test_run_command(self):
        assert self.game.run_command("a1->b2") == "Invalid Command"
        assert(False)
