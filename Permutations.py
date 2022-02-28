class Cube:
    index=['S','I','B','W']                 #stores name of cubes
    sides=["A1","A2","S3","A4","A5","A6"]   #stores name of sides
    position=0                              #stores position of cubes
    def __init__(self, index): #sides, position
        self.index=index
        # self.sides=sides
        # self.position=position

class CubeConstruct:
    shape=["XYZW"]                                     #stores the cube order
    side=[0,0,0,0,0,1]
    sides=[side,side,side,side]
    figure={"F000":[sides]}                             #stores the contacts between cubes
                                                        #following the decomposed view of a cube
    fig_name=" "
    
    def __init__(self, shape):
        self.shape=shape
        
    def stable(self):
        while_repeat=True                           #à modifier avec la valeuer du stable_prompt?
        while while_repeat==True:
            stable_prompt=input("Is this figure stable?(y/n): ")
            if stable_prompt=='y' or stable_prompt=='n' :       #à modifier
                while_repeat=False
                print(stable_prompt)
            else:
                print("Please enter y or n...")
        return stable_prompt
                
    def naming():
        fig_name=input("Name the figure: ")
        return fig_name