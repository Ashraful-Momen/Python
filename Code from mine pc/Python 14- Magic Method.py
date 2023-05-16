class Bike:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def __str__(self):

        return (f"Name: {self.name} and color: {self.color}") #Don't use print function here !!! then get type error
    
    def __eq__(self, other) :
        return self.name==other.name  and self.color == other.color
    def display(self):

        print(f"Name: {self.name} and color: {self.color}")


bike1=Bike("Yamaha", "Blue")
bike2=Bike("Yamaha","Blue")
#print(bike1)

print(bike1==bike2)