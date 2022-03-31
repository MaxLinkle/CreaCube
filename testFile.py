# -*- coding: utf-8 -*-
import itertools
#import math as m

#rules logic
#1: at least one digit
def ruleMin1Digit(listContacts):    #checks if at least one digit is present within all lists
    listBool=[False,False,False,False]
    for i in range(len(listContacts)):
        for j in range(5):
            if listContacts[i][j]!=0:
                listBool[i]=True
    if False in listBool==True:
        print("List isn't valid, no digit in list: ", listBool.index(False))
    else:
        print("List valid, every list of side has at least 1 digit")
        return True
    
#2: Min Sum=1/ Max Sum=9

def ruleMinMaxSum(listContacts):    #checks if sum of digits is at most 9 or at least 1
    sumDigits=0
    for i in range(len(listContacts)):
        for j in range(5):
            if listContacts[i][j]!=0:
                sumDigits=sumDigits+listContacts[i][j]
    if sumDigits<=9 or sumDigits>=1:
        print("List is valid, min/max=", sumDigits)
        return True
    else:
        print("List is not valid, min/max=", sumDigits)
        
#3: Max three digits; replace with rule that verifies only one list has at most 3 digits

def ruleMax3digits(listContacts):   #checks if at most 3 digits are present within a list
    listBool=[False, False, False, False]
    listDigits=[1,2,3,4]
    for i in range(len(listContacts)):
        if listDigits[i] in listContacts[i]:
            listBool[i]=True
            print("List is valid, the ", listContacts.index(listBool.index(True)), "list contains less than 4 digits")
            return True
        
#4: Digit-list correspondance

def ruleDigitListCoresp(listContacts):  #checks if a list corresponding to a digit/side contains this digit and vice-versa
    listDigits=[0,1,2,3,4]
    listBool=[False, False, False, False]
    for i in range(len(listContacts)):
        for j in range(4):
            if listDigits[j+1] in listContacts[i]:
                temp_index=listDigits[j+1]
                temp_digit=listContacts[j]                                #index() returns index of a list within the list not of a number even if it's given, needs to be given a list to return the position
    for i in range(len(listContacts)):      #change index of digit to index of list, right now you are comparing index of digit with digit brrruuuuh
        for j in range(4):
            if listContacts[temp_index][j]==temp_digit:
                listBool[i]=True
    if listBool.count(True)==4:
        print("List is valid, sides are flush")
        return True
    else:
        print("List isn't valid, this isn't a figure")
            
            
#check each list for a digit then check that digit's list to see if the digit         
            
            
#maybe use a recursive function that takes the index of a digit in a paged list as argument and uses it as an index for finding the corresponding list         

def remDuplicates_inList(target_List):
    res = []
    for i in target_List:
        if i not in res:
            res.append(i)
    return res

"""
Created on Thu Mar  3 11:50:30 2022

@author: freez
"""
#code returns permutations in a tuple inside listtaValid
#fix it by returning all perms in a tuple

temp_tupleSize1=tuple(itertools.combinations(range(1,5), 1))     #seperate digit, when converting into tuple then into list, it stays as a list eg. [[2],[3]], needs fix; fix is: use a variable(var1) to store i-th element of the tuple in var1 then use another variable(var2) to store the i-th(first and only) element of now tuple type var1 into var2 making it an int
temp_tupleSize2=tuple(itertools.combinations(range(1,5), 2))
temp_tupleSize3=tuple(itertools.combinations(range(1,5), 3))
#temp_tupleSizeAll=temp_tupleSize1+temp_tupleSize2+temp_tupleSize3
tuple1=(0,0,0,0,0)  #adapt quantity of zeroes for each tuple size
listeZero=[0,0,0,0,0]
list_PostIter=[]

#make a 'for' for each tuple1 tuple element
for i in range(len(temp_tupleSize1)):
    tuple1=tuple1+temp_tupleSize1[i]   #changed from temp_tupleSize1[0], but only the first tuple element used
    tuple_PostIter=tuple(remDuplicates_inList((itertools.permutations(tuple1, len(tuple1)))))
    tuple1=(0,0,0,0,0)
    list_PostIter.append(list(tuple_PostIter))   ##tuple isn't converted to list properly; solution: use a list to store each separate tuple value converted into a list() of the tuple into said list

tuple1=(0,0,0,0)
for i in range(len(temp_tupleSize2)):
    tuple1=tuple1+temp_tupleSize2[i]   #changed from temp_tupleSize1[0], but only the first tuple element used
    tuple_PostIter=tuple(remDuplicates_inList((itertools.permutations(tuple1, len(tuple1)))))
    tuple1=(0,0,0,0)
    list_PostIter.append(list(tuple_PostIter))

tuple1=(0,0,0)
for i in range(len(temp_tupleSize3)):
    tuple1=tuple1+temp_tupleSize3[i]   #changed from temp_tupleSize1[0], but only the first tuple element used
    tuple_PostIter=tuple(remDuplicates_inList((itertools.permutations(tuple1, len(tuple1)))))
    tuple1=(0,0,0)
    list_PostIter.append(list(tuple_PostIter))
print(list_PostIter)

list_Verif=[]
for i in range(len(list_PostIter)):
    for j in range(len(list_PostIter[i])):
        list_Verif.append(list(list_PostIter[i][j]))   #changed from temp_tupleSize1[0], but only the first tuple element used
print(list_Verif)

temp_list_Export=[]
list_model=tuple(itertools.permutations(['a','b','c','d'], 4))

# temp_tuple_Export=tuple(itertools.permutations(['a','b','c','d'], 4))
# temp_list_Export=[]
# for i in range(len(temp_list_tuple)):
#     temp_list_Export.append(temp_tuple_Export[i])
# list_permCheck=[]
# for i in list_Verif:
#     if i not in temp_list_Export:
#         list_permCheck.append(i)
# list_Verif_Export=[]    
# while list_Verif in list_permCheck==False:
#     list_Verif_Export.append(itertools.permutations(temp_list_Export[range(0,i+)]))
    




# listt=[0,1,2,3,4,0]
# listta=[listt,listt,listt,listt]
# listtaVerif=[listt,listt,listt,listt]
# list_template=[0,0,0,0,0,0]         #use as a template to insert and replace zeroes with tuples of permutations, use unpack
# temp_tuple=("elements")
# temp_tuple=list(itertools.permutations(listt, 5))   #returns permutation of elements from listta; permutations are of length 5
# temp_tupleSize1=tuple(itertools.permutations(range(1,5), 1))     #seperate digit, when converting into tuple then into list, it stays as a list eg. [[2],[3]], needs fix; fix is: use a variable(var1) to store i-th element of the tuple in var1 then use another variable(var2) to store the i-th(first and only) element of now tuple type var1 into var2 making it an int
# temp_tupleSize2=list(itertools.permutations(range(1,5), 2))
# temp_tupleSize3=list(itertools.permutations(range(1,5), 3))

# listtaVerif.clear()
# for i in range(len(list(temp_tupleSize1))):
#     temp_tupleTo1Tuple=temp_tupleSize1[i]
#     temp_tupleToInt=temp_tupleTo1Tuple[0]
#     list_template[0]=temp_tupleToInt  #insert each digit once in each position of the template list then append it to contact list
#     print("list_template=", list_template)
#     # print("List template=",list_template) /
#     # print("j=", j)                        - debug stuff
#     # print("i=", i)                        /
#     temp_TupleTemplate=remDuplicates_inList(list(itertools.permutations(list_template, 6)))  #problem: use set() then list() to delete duplicates
#     list_template=[0,0,0,0,0,0]     #problem here? maybe use clear()
#     for j in range(len(temp_TupleTemplate)):
#         listtaVerif.append(list(temp_TupleTemplate[j]))
#     # print(list_template)
#     # list_template=[0,0,0,0,0,0]
# #print(listtaVerif)

# list_template=[0,0,0,0,0]
# for k in range(len(list(temp_tupleSize2))):
#     temp_tupleTo1Tuple=temp_tupleSize2[i]
#     temp_tupleToInt[0]=temp_tupleTo1Tuple[0]
#     list_template[0]=temp_tupleToInt  #insert each digit once in each position of the template list then append it to contact list
#     print("list_template=", list_template)
#     temp_TupleTemplate=remDuplicates_inList(list(itertools.permutations(list_template, 6)))  #problem: use set() then list() to delete duplicates
#     list_template=[0,0,0,0,0,0]     #problem here? maybe use clear()
#     for j in range(len(temp_TupleTemplate)):
#         listtaVerif.append(list(temp_TupleTemplate[j]))
#     # print(list_template)
#     # list_template=[0,0,0,0,0,0]
# print(listtaVerif)

# listtaVerif.clear()    
# for i in range(119):        #119 for size of tuple containing 5 permutated elements 
#     listtaVerif.append(list(temp_tuple[i]))
#     print(listtaVerif[i])
    
# testBool=False
# for i in range(len(listtaVerif)):
#     testBool=ruleDigitListCoresp(listtaVerif)
    
# print("Valid?:", testBool)
    
            
            
            
            
            
            
            
            
            
            
# print("len subset:")
# print(len(subset))        

# for i in range(3):
#     for j in range(len(subset)):
#         listtaValid[i][j]=subset
#         print("Listta: ")
#         print(listtaValid[i][j])
        
        # if(listta[i][j]==0):
        #     listta[i][j]==1     #find how to call last element in list
                    
        #     print(listta[i][j])
            