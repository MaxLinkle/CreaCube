import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from switchcase import switch


class Conversion:

    def __init__(self, cubes):
        self.cubes = cubes

    @staticmethod
    def connected(cube, face, cube_coord):
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
    def offLimit(cube_coords):
        for coords in cube_coords.values():
            for coord in coords:
                if coord == 0:
                    if coords.index(coord) == 0:
                        for i in cube_coords.values():
                            i[0] += 1
                    elif coords.index(coord) == 1:
                        for i in cube_coords.values():
                            i[1] += 1
                    elif coords.index(coord) == 2:
                        for i in cube_coords.values():
                            i[2] += 1
                if coord == 5:
                    if coords.index(coord) == 0:
                        for i in cube_coords.values():
                            i[0] -= 1
                    elif coords.index(coord) == 1:
                        for i in cube_coords.values():
                            i[1] -= 1
                    elif coords.index(coord) == 2:
                        for i in cube_coords.values():
                            i[2] -= 1

    @staticmethod
    def coords(figure, cubes_placed, cube, cube_coord, cube_coords, previous_cube):
        index = 0
        for a in cube:
            if a != 0:
                if a not in cubes_placed:
                    cube_coord = Conversion.connected(cube, a, cube_coord)
                    cube_coords[a] = cube_coord
                    cubes_placed.append(a)
                    cube = figure.cubes[a - 1]
                    previous_cube = 0
                    break
                elif index == len(cube)-1:
                    if previous_cube == 0:
                        previous_cube = cubes_placed[len(cubes_placed) - 2]
                    else:
                        previous_cube = cubes_placed.index(previous_cube) - 1
                    break
            elif index == len(cube) - 1:
                if previous_cube == 0:
                    previous_cube = cubes_placed[len(cubes_placed) - 2]
                else:
                    previous_cube = cubes_placed.index(previous_cube) - 1
                break
            index += 1
        return cube, cube_coord, previous_cube

    @staticmethod
    def convert(figure):
        cube_coord = [1, 4, 4]
        cubes_placed = [1]
        cube_coords = {1: cube_coord}
        cube = figure.cubes[0]
        previous_cube = 0
        while len(cubes_placed) != 4:
            cube, cube_coord, previous_cube = Conversion.coords(figure, cubes_placed, cube, cube_coord, cube_coords, previous_cube)
            if previous_cube != 0:
                cube = figure.cubes[previous_cube-1]
                cube_coord = cube_coords[previous_cube]
            Conversion.offLimit(cube_coords)
        return cube_coords


class CubeDisplay:

    def __init__(self):
        self.name = None
        self.cubeOrder = None
        self.cubeOrderSym = None
        self.battery = 1
        self.sensorPosition = 1
        self.wheelsPosition = 1
        self.batteryPosition = 1
        self.solution = 0
        self.problem1 = 0
        self.problem2 = 0

    @staticmethod
    def display(figure):
        # prepare some coordinates
        x, y, z = np.indices((4, 4, 4))

        # draw cuboids in the top left and bottom right corners, and a link between them
        cube1 = (x >= figure[1][0]-1) & (x < figure[1][0]) & (y >= figure[1][1]-1) & (y < figure[1][1]) & (z >= figure[1][2]-1) & (z < figure[1][2])
        cube2 = (x >= figure[2][0]-1) & (x < figure[2][0]) & (y >= figure[2][1]-1) & (y < figure[2][1]) & (z >= figure[2][2]-1) & (z < figure[2][2])
        cube3 = (x >= figure[3][0]-1) & (x < figure[3][0]) & (y >= figure[3][1]-1) & (y < figure[3][1]) & (z >= figure[3][2]-1) & (z < figure[3][2])
        cube4 = (x >= figure[4][0]-1) & (x < figure[4][0]) & (y >= figure[4][1]-1) & (y < figure[4][1]) & (z >= figure[4][2]-1) & (z < figure[4][2])

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

        plt.savefig("fig.png")
        plt.show()

    @staticmethod
    def name(data_list):
        answer = input("Name the figure :\n")
        done = True
        while True:
            for data in data_list:
                print(data.name)
                if data.name == answer:
                    answer = input("This name already exist, please type another name :\n")
                    done = False
                    break
                else:
                    done = True
            if done:
                break
        return answer

    @staticmethod
    def balanced():
        answer = input("Is this figure balanced ? (Y/N)\n")
        while True:
            if answer == "Y":
                return True
            elif answer == "N":
                return False
            else:
                answer = input("Please, write the right answer (Y/N)\n")
