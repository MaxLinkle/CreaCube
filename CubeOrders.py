from itertools import permutations


class Order:

    def __init__(self):
        self.cubeOrders = list(permutations('BISW'))

    @staticmethod
    def attached(cube_placement, affordances, cube_orders):
        for i in range(4):
            for j in range(6):
                if cube_placement[i][j] != 0 and affordances[i][j] == 1:
                    if cube_orders[i] == 'B' or cube_orders[i] == 'S':

                    return False
        return True

    @staticmethod
    def battery_sensor():


    @staticmethod
    def rotations(cube_placement, cube_orders):
