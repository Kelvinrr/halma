import unittest
import tkinter
import sys
import os
import pytest

from .. import board
from .. import game
from .. import tree

class TestTree(unittest.TestCase):
    # def setUp(self):
    #     self.tree = tree.Tree(score=5, state=((5,5), (6,6), (1,3), (9,5)), children=None)
    #
    # # def test_repr(self):
    # #     string = self.tree.__repr__()
    # #     assert string == "Score: 5\nState: ((5, 5), (6, 6), (1, 3), (9, 5))\nChildren: None\n"
    #
    # def test_add_child(self):
    #     with self.assertRaises(Exception):
    #         self.tree.addChild(77)
    #
    #     child1 = tree.Tree(score=77, state=(5,5), children=None)
    #     child2 = tree.Tree(score=99, state=(6,6), children=None)
    #
    #     self.tree.add_child(child1)
    #     assert self.tree.children == set(child1)
    #     self.tree.add_child(child2)
    #     assert self.tree.children == set(child1,child2)
