# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:30:25 2022

@author: alvaro
"""
'''
String Methods
Strings come with a bunch of methods.
Follow the instructions closely to discover some of them.

Instructions
Use the upper() method on place and store the result in place_up.
Print out place and place_up. Did both change?
Print out the number of o's on the variable place by calling count()
on place and passing the letter 'o' as an input to the method.
We're talking about the variable place, not the word "place"!
'''
# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))
