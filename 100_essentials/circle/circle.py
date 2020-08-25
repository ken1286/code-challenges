import math

class Circle:
    # **Write your solution below**
    def __init__(self, r=1):
        self.radius = r
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    
    @property
    def area(self):
        return self.radius ** 2 * math.pi

    @area.setter
    def area(self, value):
        raise AttributeError("can't set attribute")

    def __repr__(self):
        return f"Circle({self.radius})"
    
    def __str__(self):
        return f"Circle({self.radius})"

c = Circle(2)

print(c.radius)
print(c.diameter)
print(c.area)

c.radius = 1

print(c.radius)
print(c.diameter)
print(c.area)

c.diameter = 10
print(c.radius)