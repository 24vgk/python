class ComplexNum:
    def __init__(self, num_x, num_y):
        self.num_x = num_x
        self.num_y = num_y

    def __str__(self):
        return f'({self.num_x}+{self.num_y}j)'

    def __add__(self, other):
        return ComplexNum(self.num_x + other.num_x, self.num_y + other.num_y)

    def __mul__(self, other):
        return ComplexNum(self.num_x * other.num_x, self.num_y * other.num_y)


x = ComplexNum(1, 3)
y = ComplexNum(7, 9)
print('x =', x)
print('y =', y)
print('x+y =', x + y)
print('x*y =', x * y)