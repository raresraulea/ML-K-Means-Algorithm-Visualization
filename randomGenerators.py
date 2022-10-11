import numpy as np

import constants


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
