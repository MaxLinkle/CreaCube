import csv
import xlsxwriter
from switchcase import switch


class Export:

    @staticmethod
    def rotations(cube):
        for case in switch(cube):
            if case(0):
                return "Up"
            if case(1):
                return "Down"
            if case(2):
                return "Front camera"
            if case(3):
                return "Right user"
            if case(4):
                return "Front user"
            if case(5):
                return "Left user"

    @staticmethod
    def problems(problem):
        for case in switch(problem):
            if case(1):
                return "P01-unbalance"
            if case(2):
                return "P02-rotation"
            if case(3):
                return "P03-reverse-left2right"
            if case(4):
                return "P04-reverse-outward"
            if case(5):
                return "P05-reverse-toParticipant"
            if case(6):
                return "P06-color-association"
            if case(7):
                return "P07-connection"
            if case(8):
                return "P08-doesntMove-wheels"
            if case(9):
                return "P09-doesntMove-on-off"
            if case(10):
                return "P10-doesntMove-capteur-involontaire"
            if case(11):
                return "P11-doesntMove-inverseur"
            if case(12):
                return "P12-doesntHave4cubes"

    @staticmethod
    def write(data_list):

        workbook = xlsxwriter.Workbook('data.xlsx')
        worksheet = workbook.add_worksheet()
        red = workbook.add_format()
        green = workbook.add_format()
        red.set_bg_color('red')
        green.set_bg_color('green')

        header = ['Configuration', 'Figure Name', 'CubeOrder', 'CubeOrder Symmetry', 'Battery State', 'Sensor Position', 'Wheels Position', 'Battery Position', 'Solution ?', 'Problem 1', 'Problem 2']
        col = 0
        for i in header:
            worksheet.write(0, col, i)
            col += 1

        row = 1
        config_id = 1
        for i in data_list:
            config = "config" + str(config_id)
            data = [config, i.name, i.cubeOrder]
            if i.cubeOrderSym is not None:
                data.append(i.cubeOrderSym)
            else:
                data.append('No symmetrical')

            if i.battery == 1:
                data.append("ON")
            else:
                data.append("OFF")

            data.append(Export.rotations(i.sensorPosition))
            data.append(Export.rotations(i.wheelsPosition))
            data.append(Export.rotations(i.batteryPosition))

            if i.solution == 1:
                data.append("Yes")
            else:
                data.append("No")

            data.append(Export.problems(i.problem1))

            if i.problem2 != 0:
                data.append(Export.problems(i.problem2))
            else:
                data.append('No Problem 2')

            config_id += 1

            col = 0
            for item in data:
                if item == "Yes":
                    worksheet.write(row, col, item, green)
                elif item == "No":
                    worksheet.write(row, col, item, red)
                else:
                    worksheet.write(row, col, item)
                col += 1
            row += 1

        workbook.close()
