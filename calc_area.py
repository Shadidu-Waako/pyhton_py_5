from abc import ABC, abstractmethod

class Shape(ABC):
  
  # def __init__(self, name):
  #   self.name = name
  
  @abstractmethod
  def calculate_area(self):
    pass

class Circle(Shape):
  def calculate_area(self, radius):
    self.radius = radius
    area = 3.14 * (self.radius **2)
    print(f'The area of a circle with radius {self.radius} is {area}')

class Rectangle(Shape):
  def calculate_area(self, length, width):
    self.length = length
    self.width = width
    area =  self.length * self.width
    print(f'The area of a triangle with length {self.length} and width {self.width} is {area}')

class Triangle(Shape):
  def calculate_area(self, base, height):
    self.base = base
    self.height = height
    area = 0.5 * (self.base * self.height)
    print(f'The area of a triangle with base {self.base} and height {self.height} is {area}')

circle1 = Circle()
circle1.calculate_area(int(input('Enter the radius')))

rectangle1 = Rectangle()
rectangle1.calculate_area(int(input('Enter the length')), int(input('Enter the width')))

triangle1 = Triangle()
triangle1.calculate_area(int(input('Enter the base')), int(input('Enter the height')))
  





