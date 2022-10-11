import matplotlib.pyplot as plt
import constants

from constants import *
from pltUtils import config_plt
from randomGenerators import generate_random_zone, generate_coordinate_near_average

colors = []
xPoints = []
yPoints = []

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

config_plt()

for i in range(0, dataSize):
    plt.scatter(xPoints[i],yPoints[i],c=colors[i],s=20,linewidth=0)

plt.show()
