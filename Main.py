# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 11:28:13 2022

@author: freez
"""



class Cube:
    index=['S','I','B','W']                 #stores name of cubes
    sides=["A1","A2","A3","A4","A5","A6"]   #stores name of sides
    position=0                              #stores position of cubes

class CubeConstruct:
    shape=["XYZW"]                                     #stores the cube order
    figure={"F000":[[0,0,0,0,0,0],[],[],[],[],[]]}     #stores the contacts between cubes
                                                        #following the decomposed view of a cube
    def stable(self):
        stable_prompt='e'
        while stable_prompt!='y' or stable_prompt!='n':
            print("1"+stable_prompt)
            stable_prompt=input("Is this figure stable?(y/n): ")
            print("2"+stable_prompt)
            if stable_prompt=='y' or stable_prompt=='n' :       #à modifier
                print(stable_prompt)
            else:
                print("Please enter y or n..."+stable_prompt)

obj1=CubeConstruct()
obj1.stable()