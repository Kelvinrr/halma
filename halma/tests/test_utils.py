import unittest
import tkinter
import sys
import os
import pytest
import numpy as np
from scipy.spatial.distance import cdist


from .. import board
from .. import game
from .. import tree
from .. import utils

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.points = {(1,1), (2,2), (3,3)}
        self.points2 = {(1,2), (0,1), (4,4)}
        self.camp = {(4,4), (4,3), (3,4), (3,3)}
        self.ref_point = {(0,0)}

    def test_squared_dist(self):
        assert utils.squared_dist_sum(self.ref_point, self.points) == 14.0

    def test_dist_sum(self):
        assert utils.dist_sum(self.ref_point, self.points) == 6

    def test_camp_score(self):
        assert utils.camp_score(self.points, self.camp) == [[ 3.], [ 1.], [ 2.]]

    def test_filter_camp(self):
        print(utils.filter_camp(self.camp, {(4,4)}, {(4,3)}))
        assert False
