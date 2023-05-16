i=0
while i<10:
    print(i)
    i=i+1
print("end")

i=0
while i<10:
    if i==5:
        continue #back to condition if i = 5
    print(i)
    i=i+1
print("end") # that's why this line is not executed to end line

i=0
while i<10:
    if i==5:
        break #back to condition
    print(i)
    i=i+1
print("end")