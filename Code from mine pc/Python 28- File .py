file=open("shuvo.txt","r")
print(file.readable()) #True : the file is readable
print(file.writable()) #Flase : the file is not writeable

text = file.read()

size = len(text)
print(size)

print(text)

file.close()


file2=open("shuvo.html","r")
#file2.write("\n <h1>I Love My Contry</h1>")
text2 = file2.read()
print(text2)
