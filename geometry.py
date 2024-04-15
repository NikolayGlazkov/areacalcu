import math

class Shape:
    def area(self):
        raise NotImplementedError("Этот метод должен быть переопределен")

class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        if a < 0 or b < 0 or c < 0:
            raise ValueError("Стороны не могут быть отрицательными")
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Треугольник с такими сторонами не может существовать")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def is_right_angled(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2)

def shape_factory(shape_type, *args):
    if shape_type == "circle":
        return Circle(*args)
    elif shape_type == "triangle":
        return Triangle(*args)
    else:
        raise ValueError("неизвестная форма")
    
def main():
    shapes = [
        shape_factory("circle", 5),
        shape_factory("triangle", 3, 4, 5)
    ]

    for shape in shapes:
        print(f"площадь {type(shape).__name__.lower()} is {shape.area()}")

if __name__ == "__main__":
    main()