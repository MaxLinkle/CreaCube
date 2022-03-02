import Permutations
import FigureDisplay
import ExportData

# figure = FigureDisplay.CubeDisplay("F000", [1, 4, 4], [2, 4, 4], [3, 4, 4], [2, 4, 3])
# FigureDisplay.CubeDisplay.display(figure)
# Permutations.CubeConstruct().stable()
ExportData.Export.write([{'Name': "F000",
                          'CubeOrder': "BISW",
                          'CubeOrderSym': 0,
                          'Battery': 1,
                          'SensorPosition': 2,
                          'WheelsPosition': 3,
                          'BatteryPosition': 1,
                          'Solution': 1,
                          'Problem1': 4,
                          'Problem2': 0},
                         {'Name': "F001",
                          'CubeOrder': "WISB",
                          'CubeOrderSym': "BSIW",
                          'Battery': 0,
                          'SensorPosition': 1,
                          'WheelsPosition': 4,
                          'BatteryPosition': 2,
                          'Solution': 0,
                          'Problem1': 3,
                          'Problem2': 6}])