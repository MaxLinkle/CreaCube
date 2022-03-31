import Permutations as p
import FigureDisplay
import ExportData
import CubeOrders
from copy import deepcopy

# ####find syntax to manipulate figure Var, start by trying /w one list 28/02
#
# ###Init cubes/variables
# Sensor = p.Cube('S')  # index[1]
# Button = p.Cube('B')  # index[2]
# Inverter = p.Cube('I')  # index[3]
# Wheels = p.Cube('W')  # index[4]
# nomsFigure = ["F000", "F002", "F010", "F011", "F012", "F013", "F014", "F015", "F020", "F021", "F022", "F024", "F025",
#               "F030", "F034", "F042", "F044", "F045", "F050", "F051", "F060", "F061"]
# cubeOrder = ["BISW", "BIWS", "BSIW", "BSWI", "BWSI", "IBSW", "IBWS", "BWIS", "ISBW", "ISWB", "IWBS", "IWSB", "SBIW",
#              "SBWI", "SIBW", "SWBI", "SWIB", "SIWB", "WBIS", "WBSI", "WIBS", "WISB", "WSBI", "WSIB"]
# # CubeTemplate = p.Cube(cubeOrder[1])
#
# ###Init figure
# Fxxx = p.CubeConstruct(cubeOrder[1])
# for i in range(len(nomsFigure)):
#     Fxxx.figure.update({nomsFigure[i]: Fxxx.figure})
#
# ###Permutation logic algorithm
# for i in range(6):  # i,j,k,l,n
#     # for j in range(6):
#     # for k in range()
#     if Fxxx.figure["F000":Fxxx.sides[Fxxx.side[i]]] == 1:
#         Fxxx.figure["F000":Fxxx.sides[Fxxx.side]] = 1
#
# print(Fxxx.figure)  # use object cubes to innitialise .figure to actual cubes
# # obj1=CubeConstruct()
# all_figures = [[[0, 3, 0, 0, 0, 0], [0, 0, 0, 3, 0, 0], [1, 0, 0, 4, 0, 2], [0, 0, 0, 0, 0, 3]],
#                [[0, 0, 0, 2, 0, 0], [0, 0, 0, 3, 4, 1], [0, 0, 0, 0, 0, 2], [0, 0, 2, 0, 0, 0]],
#                [[0, 0, 0, 2, 0, 0], [0, 4, 0, 3, 0, 1], [0, 0, 0, 0, 0, 3], [2, 0, 0, 0, 0, 0]],
#                [[0, 2, 0, 0, 0, 0], [1, 4, 0, 3, 0, 0], [0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0]],
#                [[0, 0, 0, 2, 3, 0], [0, 0, 0, 0, 4, 1], [0, 0, 1, 4, 0, 0], [0, 0, 2, 0, 0, 3]],
#                [[0, 3, 0, 2, 0, 0], [0, 1, 0, 0, 0, 1], [1, 0, 0, 4, 0, 0], [2, 0, 0, 0, 0, 3]],
#                [[0, 0, 0, 2, 4, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 4, 2, 0], [0, 0, 1, 0, 0, 3]],
#                [[0, 4, 0, 2, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 4, 0, 0], [1, 0, 0, 0, 0, 3]],
#                [[0, 3, 0, 0, 0, 0], [0, 4, 0, 3, 0, 0], [1, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0]],
#                [[0, 3, 0, 2, 0, 0], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 4, 0], [0, 0, 3, 0, 0, 0]],
#                [[0, 2, 0, 0, 0, 0], [1, 0, 0, 3, 4, 0], [0, 0, 0, 0, 0, 2], [0, 0, 2, 0, 0, 0]],
#                [[0, 0, 0, 0, 2, 0], [0, 4, 1, 3, 0, 0], [0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0]],
#                [[0, 2, 0, 0, 0, 0], [1, 0, 0, 0, 3, 0], [0, 0, 2, 4, 0, 0], [0, 0, 0, 0, 0, 3]],
#                [[0, 0, 0, 2, 0, 0], [0, 1, 0, 3, 0, 1], [0, 0, 0, 4, 0, 2], [0, 0, 0, 0, 0, 3]],
#                [[0, 2, 0, 0, 0, 0], [1, 3, 0, 0, 0, 0], [2, 4, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0]],
#                [[0, 0, 0, 2, 4, 0], [0, 0, 0, 3, 0, 1], [0, 0, 0, 0, 0, 2], [0, 0, 1, 0, 0, 0]],
#                [[0, 2, 0, 0, 0, 0], [1, 0, 0, 3, 0, 0], [0, 0, 0, 4, 0, 2], [0, 0, 0, 0, 0, 3]],
#                [[0, 2, 0, 0, 3, 0], [1, 0, 0, 0, 0, 0], [0, 0, 1, 4, 0, 0], [0, 0, 0, 0, 0, 3]],
#                [[0, 3, 0, 2, 0, 0], [0, 0, 0, 0, 0, 1], [1, 4, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0]],
#                [[0, 2, 0, 0, 0, 0], [1, 3, 0, 0, 0, 0], [2, 0, 0, 4, 0, 0], [0, 0, 0, 0, 0, 3]],
#                [[0, 2, 0, 0, 0, 0], [1, 0, 0, 3, 0, 0], [0, 0, 0, 0, 4, 2], [0, 0, 3, 0, 0, 0]],
#                [[0, 4, 0, 2, 0, 0], [0, 0, 0, 3, 0, 1], [0, 0, 0, 0, 0, 2], [1, 0, 0, 0, 0, 0]]]
total_figures = 0
good_figures = 0
data_list = []
cube_placement = [[0, 0, 0, 2, 3, 0], [0, 0, 0, 0, 4, 1], [0, 0, 1, 4, 0, 0], [0, 0, 2, 0, 0, 3]]
cubeOrders = CubeOrders.Order()
# for cube_placement in all_figures:
figure = FigureDisplay.Conversion(cube_placement)
figure_coords = FigureDisplay.Conversion.convert(figure)
FigureDisplay.CubeDisplay.display(figure_coords)
symmetrical = FigureDisplay.CubeDisplay.symmetrical(data_list)
if not symmetrical:
    name = FigureDisplay.CubeDisplay.name(data_list)
    balanced = FigureDisplay.CubeDisplay.balanced()
    for cubeOrder in cubeOrders.cubeOrders:
        data = FigureDisplay.CubeDisplay()
        data.name = name
        data.cubeOrder = ''.join(cubeOrder)
        good, total, data_cube_order = CubeOrders.Order.rotations(cube_placement, cubeOrder, balanced, data)
        for i in data_cube_order:
            data_list.append(deepcopy(i))
        total_figures += total
        good_figures += good
ExportData.Export.write(data_list)
print("Total Number of figures : " + str(total_figures))
print("Total number of figures that can be solutions (4 cubes connected, battery on, balanced, wheels down) : " + str(good_figures))
# Permutations.CubeConstruct().stable()
# ExportData.Export.write([{'Name': "F000",
#                           'CubeOrder': "BISW",
#                           'CubeOrderSym': 0,
#                           'Battery': 1,
#                           'SensorPosition': 2,
#                           'WheelsPosition': 3,
#                           'BatteryPosition': 1,
#                           'Solution': 1,
#                           'Problem1': 4,
#                           'Problem2': 0},
#                          {'Name': "F001",
#                           'CubeOrder': "WISB",
#                           'CubeOrderSym': "BSIW",
#                           'Battery': 0,
#                           'SensorPosition': 1,
#                           'WheelsPosition': 4,
#                           'BatteryPosition': 2,
#                           'Solution': 0,
#                           'Problem1': 3,
#                           'Problem2': 6}])
