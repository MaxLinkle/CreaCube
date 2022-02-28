import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


class CubeDisplay:

    def __init__(self, name, cube1, cube2, cube3, cube4):
        self.name = name
        self.cube1 = cube1
        self.cube2 = cube2
        self.cube3 = cube3
        self.cube4 = cube4

    @staticmethod
    def display(figure):
        # prepare some coordinates
        x, y, z = np.indices((4, 4, 4))

        # draw cuboids in the top left and bottom right corners, and a link between them
        cube1 = (x >= figure.cube1[0]-1) & (x < figure.cube1[0]) & (y >= figure.cube1[1]-1) & (y < figure.cube1[1]) & (z >= figure.cube1[2]-1) & (z < figure.cube1[2])
        cube2 = (x >= figure.cube2[0]-1) & (x < figure.cube2[0]) & (y >= figure.cube2[1]-1) & (y < figure.cube2[1]) & (z >= figure.cube2[2]-1) & (z < figure.cube2[2])
        cube3 = (x >= figure.cube3[0]-1) & (x < figure.cube3[0]) & (y >= figure.cube3[1]-1) & (y < figure.cube3[1]) & (z >= figure.cube3[2]-1) & (z < figure.cube3[2])
        cube4 = (x >= figure.cube4[0]-1) & (x < figure.cube4[0]) & (y >= figure.cube4[1]-1) & (y < figure.cube4[1]) & (z >= figure.cube4[2]-1) & (z < figure.cube4[2])

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
