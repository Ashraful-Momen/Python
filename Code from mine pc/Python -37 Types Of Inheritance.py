class A:
     def display1(self):
        print("I am in A class")


class B(A):
    def display2(self):
        print("I am in B class")


class C(B):

    def display3(self):
        super().display1()
        super().display2()
        print("I am in C class")


obj1 = C()
obj1.display3()
print("===================")


class D(C, B, A):

    def display4(self):
        super().display1()
        super().display2()
        super().display3()
        print("I am in D class")


obj2 = D()
obj2.display4()
print("===================")


class E(D):
    pass


obj3 = E()
obj3.display4()



