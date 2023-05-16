
num = input("Enter digits ")
list = num.split()

sum = 0

for x in list:

    sum=sum+int(x)
print("The some of list digits is : ", sum)

#-------------------------------------------------------
print("Enter another string: ")

latter = input("Plz wirte down: ")

Alpha=0
word=0
digit=0
for x in latter:
    x=x.lower()
    if x >= "0" and  x<= "9" :
        digit=digit+1
    elif x >= "a" and x <="z":
        Alpha=Alpha+1
    elif x == " ":
        word=word+1
print("Total digit is : ", digit)
print("Total word is : ", word+1)
print("Total ALpha is : ", Alpha)