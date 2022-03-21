from itertools import permutations
from switchcase import switch


class Order:

    def __init__(self):
        self.cubeOrders = list(permutations('BISW'))

    @staticmethod
    def attached(cube_placement, affordances, cube_orders):
        for i in range(4):
            for j in range(6):
                if cube_placement[i][j] != 0 and affordances[i][j] == 1:
                    if cube_orders[i] == 'B' or cube_orders[i] == 'S':
                        for k in cube_placement[i]:
                            if k != 0 and k != cube_placement[i][j]:
                                if cube_placement[k][j] != 0:
                                    face = 0
                                    for l in cube_placement[k]:
                                        if l == i:
                                            face = l
                                    if cube_placement[cube_placement[k][j]][face] != 0:
                                        return True
                    return False
        return True

    @staticmethod
    def affordances(cube, position, data):
        affordance = 0
        for i in position:
            if i == 0:
                affordance = position.index(i)
        for case in switch(cube):
            if case('S'):
                data.sensorPosition = affordance
            if case('W'):
                data.wheelsPosition = affordance
            if case('B'):
                data.batteryPosition = affordance

    @staticmethod
    def rotations(cube_placement, cube_order, balanced, data):
        affordances_base = [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
        affordances = []
        total_cube_orders = []
        data_list = []
        cubes_affordances = [1, 2, 3, 4]
        good = 0
        total = 0
        while True:
            if not affordances:
                for i in range(4):
                    if cube_order[i] == 'I':
                        cubes_affordances.pop(i)
                        affordances.append(affordances_base[0])
                    else:
                        affordances.append(affordances_base[1])
                        Order.affordances(cube_order[i], affordances_base[1], data)
                total_cube_orders.append(affordances)
                data_list.append(data)
            else:
                if affordances_base.index(affordances[cubes_affordances[0]]) != 6:
                    affordances[cubes_affordances[0]] = affordances_base[affordances_base.index(
                        affordances[cubes_affordances[0]]) + 1]
                    Order.affordances(cube_order[cubes_affordances[0]],
                                      affordances[cubes_affordances[0]], data)
                    if affordances in total_cube_orders:
                        break
                    else:
                        total_cube_orders.append(affordances)
                        data_list.append(data)
                else:
                    affordances[cubes_affordances[0]] = affordances_base[1]
                    Order.affordances(cube_order[cubes_affordances[0]], affordances_base[1], data)
                    if affordances in total_cube_orders:
                        break
                    else:
                        total_cube_orders.append(affordances)
                        data_list.append(data)
                    if affordances_base.index(affordances[cubes_affordances[1]]) != 6:
                        affordances[cubes_affordances[1]] = affordances_base[affordances_base.index(
                            affordances[cubes_affordances[1]]) + 1]
                        Order.affordances(cube_order[cubes_affordances[1]],
                                          affordances[cubes_affordances[1]], data)
                        if affordances in total_cube_orders:
                            break
                        else:
                            total_cube_orders.append(affordances)
                            data_list.append(data)
                    else:
                        affordances[cubes_affordances[1]] = affordances_base[1]
                        Order.affordances(cube_order[cubes_affordances[1]], affordances_base[1], data)
                        if affordances in total_cube_orders:
                            break
                        else:
                            total_cube_orders.append(affordances)
                            data_list.append(data)
                        if affordances_base.index(affordances[cubes_affordances[2]]) != 6:
                            affordances[cubes_affordances[2]] = affordances_base[affordances_base.index(
                                affordances[cubes_affordances[2]]) + 1]
                            Order.affordances(cube_order[cubes_affordances[2]],
                                              affordances[cubes_affordances[2]], data)
                            if affordances in total_cube_orders:
                                break
                            else:
                                total_cube_orders.append(affordances)
                                data_list.append(data)
                        else:
                            affordances[cubes_affordances[2]] = affordances_base[1]
                            Order.affordances(cube_order[cubes_affordances[2]], affordances_base[1], data)
                            if affordances in total_cube_orders:
                                break
                            else:
                                total_cube_orders.append(affordances)
                                data_list.append(data)

            attached = Order.attached(cube_placement, affordances, cube_order)

            if attached and balanced:
                good += 1
                data.solution = 1
            total += 1

        for i in data_list:
            print(vars(i))

        return good, total, data_list
