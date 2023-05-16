class Triangle:
    base = " "
    height = ""

    def __init__(self,base,height):
        self.base = base
        self.height = height

    def display(self):
        print(f" Base: {self.base} and Height : {self.height} = Area {self.base * self.height} ")


area = Triangle(2, 4)
area.display()

