from abc import ABC, abstractmethod

class Shape(ABC):
  
  def __init__(self, name):
    self.name = name
  
  @abstractmethod
  def calculate_area(self):
    pass

class Circle(Shape):
  def __init__(self, name):
    super().__init__(name)
    self.name = name
    
  def calculate_area(self, radius):
    self.radius = radius
    area = 3.14 * (self.radius **2)
    print(f'The area of a circle with radius {self.radius} is {area}\n')

class Rectangle(Shape):
  def __init__(self, name):
    super().__init__(name)
    self.name = name

  def calculate_area(self, length, width):
    self.length = length
    self.width = width
    area =  self.length * self.width
    print(f'The area of a triangle with length {self.length} and width {self.width} is {area}\n')

class Triangle(Shape):
  def __init__(self, name):
    super().__init__(name)
    self.name = name

  def calculate_area(self, base, height):
    self.base = base
    self.height = height
    area = 0.5 * (self.base * self.height)
    print(f'The area of a triangle with base {self.base} and height {self.height} is {area}\n')


input_number_of_times = int(input('Enter the number of times: '))
for i in range(input_number_of_times):
  print(f'\nENTER DETAILS OF CIRCLE🟢-{i + 1}')
  circle1 = Circle('Circle')
  circle1.calculate_area(int(input('Enter the radius: ')))

  print(f'ENTER DETAILS OF RECTANGLE🟪-{i + 1}')
  rectangle1 = Rectangle('Rectangle')
  rectangle1.calculate_area(int(input('Enter the length: ')), int(input('Enter the width: ')))

  print(f'ENTER DETAILS OF TRIANGLE🔺-{i + 1}')
  triangle1 = Triangle('Triangle')
  triangle1.calculate_area(int(input('Enter the base: ')), int(input('Enter the height: ')))
