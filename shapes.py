
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        result=22/7*(self.radius*self.radius)
        return result
    def calculate_circumference(self):
        cir=2*(22/7*self.radius)
        print(cir)

class Square:
    def __init__(self,side):
        self.side=side
    def area(self):
        area_square=self.side**2
        return area_square
    def perimeter(self):
        perimeter_square=4*self.side
        return perimeter_square

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        rect_area=self.length*self.width
        return rect_area
    def perimeter_rectangle(self):
        rect_perimeter=2*(self.length + self.width)
        return rect_perimeter

class Sphere:
    def __init__(self,radius_sphere):
        self.radius_sphere=radius_sphere
    def surface_area(self):
        surf_area=4*(22/7*(self.radius_sphere**2))
        return surf_area
    def volume(self):
        sphere_volume=4/3*(22/7*(self.radius_sphere**3))
        return sphere_volume       