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


def draw_centroids():
    cx_points = []
    cy_points = []
    for c in centroids:
        cx_points.append(c.x)
        cy_points.append(c.y)

    config_plt()
    for i in range(0, constants.dataSize):
        plt.scatter(xPoints[i], yPoints[i], c=colors[i], s=20, linewidth=0)

    plt.scatter(cx_points, cy_points, c='yellow')

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

all_points_x = []
all_points_y = []
colors2 = []
for i in range(-300, 300):
    for j in range(-300, 300):
        all_points_x.append(i)
        all_points_y.append(j)
        current_point = Point(i, j)
        similarityWith = {}
        for final_centroid in centroids:
            similarity = similarities.get_euclidian_distance_similarity(current_point, final_centroid)
            similarityWith[final_centroid.index] = similarity
        best_centroid_index = min(similarityWith, key=similarityWith.get)
        best_centroid = next(x for x in centroids if x.index == best_centroid_index)
        colors2.append(best_centroid.color)


config_plt()
for i in range(0, constants.dataSize):
    plt.scatter(xPoints[i], yPoints[i], c=colors[i], s=20, linewidth=0)


def get_neighbours(i, j):
    result = []
    if i == 0 or i == 599 or j == 0 or j == 599:
        if i != 0:
            result.append(600*(i-1) + j)
        if j != 0:
            result.append(600*i + j - 1)
        if i != 599:
            result.append(600*(i+1) + j)
        if j != 599:
            result.append(600*i + j + 1)
    return result

draw_centroids()

for index, color in enumerate(colors2):
    if index + 1 < len(colors2) and not color == colors2[index + 1]:
        plt.scatter(all_points_x[index], all_points_y[index], c=color, s=20, linewidth=0)

# for i in range(0, 599):
#     for j in range(0, 599):
#         current_index = i*600 + j
#         print('CI: ', colors2[current_index])
#         top_neighbour = (i-1)*600 + j
#         left_neighbour = current_index - 1
#         right_neighbour = current_index + 1
#         bottom_neighbour = (i+1)*600 + j
#         neighbours = get_neighbours(i, j)
#         should_display = 1
#         for n in neighbours:
#             colors2[current_index] == colors2[n]
#         if not colors2[top_neighbour] == colors2[current_index] and not colors2[left_neighbour] == colors2[current_index] and not colors2[bottom_neighbour] == colors2[current_index] and not colors2[right_neighbour] == colors2[current_index]:
#             print('POINT')
#             plt.scatter(all_points_x[current_index], all_points_y[current_index], c=colors2[current_index], s=20, linewidth=0)
plt.show()

# display_plot_with_data()
# for c in centroids:
#     print(c.x, c.y)
