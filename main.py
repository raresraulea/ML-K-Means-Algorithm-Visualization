import matplotlib.pyplot as plt

from Point import Point
from pltUtils import display_plot_with_data
from pltUtils import config_plt
from randomGenerators import generate_new_data, generate_random_number_of_centroids

# generate_new_data()
# config_plt()
# display_plot_with_data()

points = []

# read points and generate array
with open('data.txt') as f:
    lines = f.readlines()
    for line in lines:
        words = line.split()
        points.append(Point(float(words[0]), float(words[1])))

centroids = []
n_of_centroids = generate_random_number_of_centroids()
for i in range(1, n_of_centroids):
    rand_x =

print(n_of_centroids)
