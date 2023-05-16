#This is set
'''
num2 = (1,1,2,3) tuple
print(num2)

num3 = [1,2,2,3] list
print(num3)
'''



num1 ={10,2,3,3} # no duplicate value will print
print(num1)
num2= set([1,2,3,4,5])
print(num2)
num1.add(8)
num2.remove(3)
# mainly use for set operation: and , or , subtraction :
print(num1 | num2)
print(num2 & num1)
print(num1 - num2)