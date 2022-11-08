import math

from Centroid import Centroid
from Point import Point


def get_euclidian_distance_similarity(x1: Point, centroid: Centroid):
    return math.sqrt((x1.y - centroid.y)*(x1.y - centroid.y) + (x1.x - centroid.x)*(x1.x - centroid.x))
