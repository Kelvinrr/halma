import numpy as np
from scipy.spatial.distance import cdist
import functools

def least_square(a, b):
    return np.linalg.lstsq(a,b)

def squared_dist_sum(ref_point, points):
    """
    """
    return np.sum((cdist(list(points), list(ref_point), metric='cityblock')/2)**2)

def dist_sum(ref_point, points):
    """
    """
    return np.sum(cdist(list(points), list(ref_point), metric='cityblock')/2)

def camp_score(points, camp):
    points, camp = list(points), list(camp)
    def get_camp_goal(point):
        return max(cdist(camp, [point],metric='cityblock')/2)

    return np.sum(np.apply_along_axis(get_camp_goal, 1, points)**2)

def filter_camp(camp, *args):
    return camp - set.union(*args)
