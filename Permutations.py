
class Cube:
    index = ['S', 'I', 'B', 'W']  # stores name of cubes
    sides = ["A1", "A2", "A3", "A4", "A5", "A6"]  # stores name of sides
    position = 0  # stores position of cubes


class CubeConstruct:
    shape = ["XYZW"]  # stores the cube order
    figure = {"F000": [[0, 0, 0, 0, 0, 0], [], [], [], [], []]}  # stores the contacts between cubes

    # following the decomposed view of a cube
    @staticmethod
    def stable():
        while_repeat = True  # à modifier avec la valeur du stable_prompt?
        while while_repeat:
            stable_prompt = input("Is this figure stable?(y/n): ")
            if stable_prompt == 'y' or stable_prompt == 'n':  # à modifier
                while_repeat = False
                print(stable_prompt)
            else:
                print("Please enter y or n...")

# Sensor=Cube()
# Button=Cube()
# Inverter=Cube()
# Wheels=Cube()
