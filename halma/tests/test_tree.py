import unittest
import tkinter
import sys
import os
import pytest

from .. import board
from .. import game
from .. import tree

class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = tree.Tree(score=5, state=((5,5), (6,6), (1,3), (9,5)), children=None)

    def test_repr(self):
        string = self.tree.__repr__()
