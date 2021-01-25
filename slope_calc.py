# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:35:47 2021

@author: James
"""

class Point:
    #Create a new point at coordinates x y
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance_from_origin(self): #Distance from origin
        return((self.x**2) + (self.y**2))**0.5
    
    def __str__(self): #Print the point
        return "({0}, {1})".format(self.x, self.y)
    
    def slope_from_origin(self): #returns slope of the line joining origin to point
        if self.x != 0: #if x does not equal zero
            return(self.y/self.x) #divide y by x
        elif self.x < 0: #else if x is lower than 0
            return(-0.0) #return -0.0
        else: #else return false
            return(False)
    def get_line_to(self,p): #returns straight line equation between one point object and another point
        if self.x - p.x != 0: #make sure no zeros are equal
            a = (self.y - p.y)/(self.x - p.x) #divide for a
            b = (self.x*p.y - p.x*self.y)/(self.x-p.x) #calculate b
            if b == 0:
                return(a, -b)
            else:
                return(a, b)
        else:
            return(False)

