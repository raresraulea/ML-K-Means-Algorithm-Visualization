from matplotlib import pyplot as plt

import constants


def config_plt():
    plt.rcParams["figure.figsize"] = [10, 7]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    plt.axis([constants.xAxisMin, constants.xAxisMax, constants.yAxisMin, constants.yAxisMax])