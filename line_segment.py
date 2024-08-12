# Author: Jake Trissel
# Github Username: trisselj
# Date: 08/07/2024
# Description: Defines a Point class for representing 2D coordinates and calculating the distances between points, along with a LineSegment class that uses the points to compute the length, slope, and parallelism of the line segments.

class Point: # Initializing the class
    def __init__(self, x_coord, y_coord): #INitializing the private x and y coords
        self._x_coord = x_coord
        self._y_coord = y_coord
    
    def get_x_coord(self): # Return for the x
        return self._x_coord
    
    def get_y_coord(self): # Return for the y
        return self._x_coord
    
    def distance_to(self, other_point): # Calculates and returns the distance to another point object
        return ((other_point.get_x_coord() - self._x_coord) ** 2 + (other_point.get_y_coord() - self._y_coord) ** 2) ** 0.5
    
class LineSegment: # Initializes the class
    def __init__(self, endpoint_1, endpoint_2): # Initializes the private endpoints of the line segment
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2
    
    def get_endpoint_1(self): # Returns the first endpoint
        return self._endpoint_1

    def get_endpoint_2(self): # Returns the second endpoint
        return self._endpoint_2

    def length(self): # Calculates and returns the length of the linesegment 
        return self._endpoint_1.distance_to(self._endpoint_2)

    def slope(self): # Calculates and returns the slope of the linesegment
        x1 = self._endpoint_1.get_x_coord()
        y1 = self._endpoint_1.get_y_coord()
        x2 = self._endpoint_2.get_x_coord()
        y2 = self._endpoint_2.get_y_coord()
        return (y2 - y1) / (x2 - x1)

    def is_parallel_to(self, other_line): # Returns the line segment as True (parallel) if the difference in slope is less than 0.000001
        return abs(self.slope() - other_line.slope()) < 0.000001