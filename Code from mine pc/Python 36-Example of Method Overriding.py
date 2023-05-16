class Shape:
    def __init__(self, dim1, dim2):  #don't miss the spelling of  "init" #then get typerror
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("The Area is : ")


class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Ans of the Triangle", area)


janina = Triangle(10, 20)
janina.area()
print(isinstance(janina,Triangle))
