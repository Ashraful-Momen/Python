#================alter native map () : 1 line===========
#
num=[1,2,3,4,5]

#result = [condition for x in list]
result = [x*x for x in num]
print(result)

#===================== alternative filter (): 1 line============

num=[1,2,3,4,5]

#result = [condition for x in list]
result = [x for x in num if x%2==0]
print(result)