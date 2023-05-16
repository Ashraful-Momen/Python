#Zip : combiand 2 list into a list by tuple ways
id = [1,2,3,4]
name = [ "shuvo", "Ahsraful"," Momen "]

result = list(zip(id,name))
result = list(zip(id,name,"ABCDEF")) # Must be use "" to print ABCDEF
print(result)