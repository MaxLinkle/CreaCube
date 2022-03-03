import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from switchcase import switch


class Conversion:

    def __init__(self, cubes):
        self.cubes = cubes

    @staticmethod
    def connected(cube, face, cube_coord):
        print(cube)
        for case in switch(cube.index(face)):
            if case(0):
                return [cube_coord[0], cube_coord[1], cube_coord[2] + 1]
            if case(1):
                return [cube_coord[0], cube_coord[1], cube_coord[2] - 1]
            if case(2):
                return [cube_coord[0], cube_coord[1] - 1, cube_coord[2]]
            if case(3):
                return [cube_coord[0] + 1, cube_coord[1], cube_coord[2]]
            if case(4):
                return [cube_coord[0], cube_coord[1] + 1, cube_coord[2]]
            if case(5):
                return [cube_coord[0] - 1, cube_coord[1], cube_coord[2]]

    @staticmethod
    def coords(figure, cubes_placed, cube, cube_coord, cube_coords):
        for i in figure.cubes[cube-1]:
            if i != 0:
                if i not in cubes_placed:
                    cube_coord = Conversion.connected(figure.cubes[cube-1], i, cube_coord)
                    cube_coords.append(cube_coord)
                    cubes_placed.append(i)
                    cube = i
                    Conversion.coords(figure, cubes_placed, cube, cube_coord, cube_coords)

    @staticmethod
    def convert(figure):
        cube_coord = [1, 4, 4]
        cube_coords = [cube_coord]
        cubes_placed = [1]
        cube = 1
        Conversion.coords(figure, cubes_placed, cube, cube_coord, cube_coords)
        return cube_coords


class CubeDisplay:

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
