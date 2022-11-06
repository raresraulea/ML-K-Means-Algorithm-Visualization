import numpy as np

import constants

colors = []
xPoints = []
yPoints = []


def gauss(x, m):
    return np.exp(-1 / 2 * np.square((m - x) / constants.sigma))


def generate_coordinate_near_average(average):
    while 1:
        randomCoordinate = np.random.uniform(-300, 300)
        gaussResult = gauss(randomCoordinate, average)
        randomThreshold = np.random.randint(0, 1000)/1000

        if gaussResult >= randomThreshold:
            if gaussResult == 0:
                print(gaussResult)
            return randomCoordinate


def generate_random_zone():
    randomZoneIndex = np.random.randint(0, constants.numberOfZones)
    return constants.zones[randomZoneIndex], randomZoneIndex


def generate_new_data():
    with open('data.txt', 'a') as f:
        for i in range(constants.dataSize):
            (zoneX, zoneY, zoneColor), zoneIndex = generate_random_zone()
            colors.append(zoneColor)
            randomXCoord = generate_coordinate_near_average(zoneX)
            xPoints.append(randomXCoord)
            randomYCoord = generate_coordinate_near_average(zoneY)
            yPoints.append(randomYCoord)
            newRow = "{} {} {} \n".format(randomXCoord, randomYCoord, zoneIndex)
            f.write(newRow)


def generate_random_number_of_centroids():
    return np.random.randint(constants.minCentroids, constants.maxCentroids)