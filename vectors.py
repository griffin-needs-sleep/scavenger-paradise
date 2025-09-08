import math

class vec():
    def __init__(self, x:int|float, y:int|float) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, v):
        return vec(v.x+self.x, v.y+self.y)
    
    def __sub__(self, v):
        return vec(self.x-v.x, self.y-v.y)
    
    def __mul__(self, f):
        return vec(self.x*f, self.y*f)
    
    def __rmul__(self, f):
        return vec(self.x*f, self.y*f)
    
    def __abs__(self):
        return math.sqrt(self.x**2+self.y**2)
    
    def __str__(self):
        return f"vec({self.x}, {self.y})"
    
    def __iter__(self):
        return [self.x, self.y].__iter__()

