def suqar(x):
    return x*x

print(suqar(2))

# lamda peramiter: expression (value,value,.....)

cube =  (lambda x : x * x * x ) (2)
print(cube)

#a+b*2
print((lambda a,b: a*a+2*a*b+b*b)(2,2))