def sum(*num): #xarg is working as(tuple ) for same data type oparetion
    add=0
    for x in num:
        add=add+x
    print(add)
print("enter noumber for add")

sum(10,20)
sum(20,30,40)

def student(**details):   #xxarg: working as dictionary : need keyvalue to print
    print(details)
    print(details["id"])
    print(details["name"])
student(id=101,name="Shuvo")
student(id=102,name="Ashraful",aname="Shuvo")