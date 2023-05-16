from abc import ABC , abstractmethod

class Shape(ABC):  #Must be use (ABC) other ways abstruct is not working
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("The Triangle Area is : ",area)

#obj=Shap() #abs() can't use in main class but other class can use which is inherited

obj=Triangle(20,30)
obj.area()