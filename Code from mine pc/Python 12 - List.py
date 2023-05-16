item=['c','c++','java','python',"javascript"]

print(item)
print(item[-1])
print(item[2:])

print("python" in item)
print("go" in item)
print("go" not in item) ## in and 'not in' is a boolean oparetor

print(item + ['shuvo',38]) #add item

print(item*5)
#-------------------------------List function------------------#
item.append("Momen")
print(item)
item.insert(2,"ruby")
item.remove("java")
item.sort()
item2=[1,4,0,3,4]
item2.reverse()
print(item2)
print(item2.count(4))
item2.sort()
print(item2)
pos =item2.index(3)
print(f"{3}: it's the item index position is {pos}")
item2.pop(3)
print(item2)