import csv
from switchcase import switch


class Export:

    @staticmethod
    def write(data_list):
        # CSV header
        header = ['Configuration', 'Figure Name', 'CubeOrder', 'CubeOrder Symmetry', 'Wheels Position', 'Battery State', 'Sensor Position', 'Solution ?', 'Problem 1', 'Problem 2']

        with open('data.csv', 'w', encoding='UTF8', newline='') as f:

            # Create the CSV writer
            writer = csv.writer(f)

            # Write the header
            writer.writerow(header)

            config_id = 1
            for i in data_list:
                config = "config" + str(config_id)
                data = [config, i["Name"], i["CubeOrder"]]
                if i["CubeOrderSym"] != 0:
                    data.append(i["CubeOrderSym"])
                if i["Wheels"] == 1:
                    data.append("Down")
                else:
                    data.append("Not down")
                if i["Battery"] == 1:
                    data.append("ON")
                else:
                    data.append("OFF")

                for case in switch(i["SensorPosition"]):
                    if case(0):
                        data.append("Up")
                    if case(1):
                        data.append("Down")
                    if case(2):
                        data.append("Front camera")
                    if case(3):
                        data.append("Right user")
                    if case(4):
                        data.append("Front user")
                    if case(5):
                        data.append("Left user")

                if i["Solution"] == 1:
                    data.append("Yes")
                else:
                    data.append("No")

                for x in range(2):
                    for case in switch(i["Problem"+str(x+1)]):
                        if case(0):
                            data.append("Unbalance")
