import math
import statistics

class Circle:

    def __init__(self, radius = 1):
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * radius
    
    def get_area(self):
        return math.pi * math.pow(radius, 2)

    def set_radius(self, radius):
        self.radius = radius

    
####################

class Math_Check:

    def__init__(self, min, max, mean):
        self.min = min
        self.max = max
        self.mean = mean

    def min(self):

class Storage:

    @staticmethod
    def store(**kwargs):
        
        data = json.dumps(kwargs)
        file = open("acct_db", "w")
        file.write(data)
