# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:43:34 2022

@author: alvaro
"""
'''
Instead of creating a flat list containing strings and floats,
representing the names and areas of the rooms in your house,
you can create a list of lists.
The script in the editor can already give you an idea.

Example,
Don't get confused here: "hallway" is a string,
while hall is a variable that represents the float 11.25 you specified earlier.
'''

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))