import numpy as np
from numpy.linalg import norm
from scipy.spatial.distance import cdist
import functools

from numpy import arccos, array, dot, pi
from numpy.linalg import det, norm

def least_square(a, b):
    return np.linalg.lstsq(a,b)

def squared_dist_sum(ref_point, points):
    """
    """
    return np.sum((cdist(list(points), [list(ref_point)], metric='euclidean'))**2)

def dist_sum(ref_point, points):
    """
    """
    return np.sum(cdist(list(points), [list(ref_point)], metric='euclidean'))

def camp_score(points, camp):
    points, camp = list(points), list(camp)
    def get_camp_goal(point):
        return max(cdist(camp, [point],metric='euclidean'))

    return np.sum(np.apply_along_axis(get_camp_goal, 1, points)**2)

def filter_camp(player, *args):
    ret = player.goal - set.union(*args)
    print(ret)
    return ret if ret else [player.goalTile]

def line_score(points, team_goal, opp_goal ):
    points,team_goal,opp_goal = np.asarray(list(points)), np.asarray(list(team_goal)), np.asarray(list(opp_goal))
    print(points)
    def dist_to_line(P):
        """ segment line AB, point P, where each one is an array([x, y]) """
        A = team_goal
        B = opp_goal
        if all(A == P) or all(B == P):
            return 0
        if arccos(dot((P - A) / norm(P - A), (B - A) / norm(B - A))) > pi / 2:
            return norm(P - A)
        if arccos(dot((P - B) / norm(P - B), (A - B) / norm(A - B))) > pi / 2:
            return norm(P - B)
        print(abs(dot(A - B, P[::-1]) + det([A, B])) / norm(A - B))
        return abs(dot(A - B, P[::-1]) + det([A, B])) / norm(A - B)

    return np.sum(np.apply_along_axis(dist_to_line, 1, points)**2)
