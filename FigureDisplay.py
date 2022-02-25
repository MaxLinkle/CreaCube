import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


class CubeDisplay:

    @staticmethod
    def display():
        # x, y, z = np.indices((4, 4, 4))
        # cube1 = (x < 1) & (y > 3) & (z > 3)
        # voxels = cube1
        # colors = np.empty(voxels.shape, dtype=object)
        # colors[cube1] = 'red'
        # fig = plt.figure()
        # ax = fig.gca(projection='3d')
        # ax.voxels(voxels, facecolors=colors, edgecolors='k')
        # plt.show()
        # prepare some coordinates
        x, y, z = np.indices((4, 4, 4))

        # draw cuboids in the top left and bottom right corners, and a link between them
        cube1 = (x < 1) & (y >= 3) & (z >= 3)
        cube2 = (x >= 1) & (x < 2) & (y >= 3) & (z >= 3)
        cube3 = (x >= 2) & (x < 3) & (y >= 3) & (z >= 3)
        cube4 = (x >= 1) & (x < 2) & (y >= 3) & (z >= 2) & (z < 3)

        # combine the objects into a single boolean array
        voxels = cube1 | cube2 | cube3 | cube4

        # set the colors of each object
        colors = np.empty(voxels.shape, dtype=object)
        colors[cube1] = 'grey'
        colors[cube2] = 'grey'
        colors[cube3] = 'grey'
        colors[cube4] = 'grey'

        # and plot everything
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.voxels(voxels, facecolors=colors, edgecolor='k')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_zticklabels([])

        plt.show()