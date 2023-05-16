

class Student:
    id = " "
    name = " "

    def set_value(self,id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"Id: {self.id} and Name : {self.name}")


obj = Student()
#print(isinstance(obj, Student)) #check the object of class

#obj.id = 101
#obj.name = "Shvuo"
#print(f"Id: {obj.id} and Name: {obj.name}")

obj.set_value(101, "Ashraful")
obj.display()
