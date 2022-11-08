from matplotlib import pyplot as plt

import constants
import similarities
from Centroid import Centroid
from Point import Point
import numpy as np

from pltUtils import config_plt, display_plot_with_data
from randomGenerators import generate_new_data, generate_random_number_of_centroids, colors, yPoints, xPoints

# generate_new_data()

points = []
E = 0
new_E = -1

# config_plt()
# for i in range(0, constants.dataSize):
#     plt.scatter(xPoints[i], yPoints[i], c=colors[i], s=20, linewidth=0)

# read points and generate array
with open('data.txt') as f:
    lines = f.readlines()
    for line in lines:
        words = line.split()
        points.append(Point(float(words[0]), float(words[1])))
    if len(colors) == 0:
        colors = list(map(lambda l: constants.zones[int(l.split()[2])][2], lines))
if len(xPoints) == 0:
    xPoints = list(map(lambda p: p.x, points))
    yPoints = list(map(lambda p: p.y, points))

# generate cetroids and initialize them
centroids = []
n_of_centroids = generate_random_number_of_centroids()
random_indexes = []

# generate k random indexes
while len(random_indexes) < n_of_centroids:
    new_index = np.random.randint(0, len(points) - 1)
    if not random_indexes.__contains__(new_index):
        random_indexes.append(new_index)

# select centroid from the points array at the random indexes created before
for index, indexValue in enumerate(random_indexes):
    point = points[indexValue]
    centroid = Centroid(point.x, point.y, index, constants.available_colors[index])
    centroids.append(centroid)


print(colors)
while not new_E == E:
    E = new_E
    # init centroids with no points
    centroids_with_points = {}
    for centroid in centroids:
        centroids_with_points[centroid.index] = []

    # collect points for each centroid
    for idx, point in enumerate(points):
        similarityWith = {}
        for centroid in centroids:
            similarity = similarities.get_euclidian_distance_similarity(point, centroid)
            similarityWith[centroid.index] = similarity
        best_centroid = min(similarityWith, key=similarityWith.get)
        current_centroid = next(x for x in centroids if x.index == best_centroid)
        print(current_centroid.color)
        colors[idx] = current_centroid.color
        centroids_with_points[best_centroid].append(point)

    new_centroids = []
    new_E = 0
    for centroidIndex in centroids_with_points:
        average_x = 0
        average_y = 0
        inner_sum = 0
        for point in centroids_with_points[centroidIndex]:
            current_centroid = next(x for x in centroids if x.index == centroidIndex)
            average_x += point.x
            average_y += point.y
            inner_sum += similarities.get_euclidian_distance_similarity(point, current_centroid)
        new_E += inner_sum
        average_x /= len(centroids_with_points[centroidIndex])
        average_y /= len(centroids_with_points[centroidIndex])
        current_centroid = next(x for x in centroids if x.index == centroidIndex)
        new_centroids.append(Centroid(average_x, average_y, centroidIndex, current_centroid.color))

    centroids = new_centroids

    cx_points = []
    cy_points = []
    for c in centroids:
        cx_points.append(c.x)
        cy_points.append(c.y)

    config_plt()
    for i in range(0, constants.dataSize):
        plt.scatter(xPoints[i], yPoints[i], c=colors[i], s=20, linewidth=0)

    plt.scatter(cx_points, cy_points, c='yellow')
    plt.show()

    print(new_E)


# display_plot_with_data()
# for c in centroids:
#     print(c.x, c.y)
