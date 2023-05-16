studenId = {

    101 : "Ashraful ",  # use ':' not but not use "=" in dictionary
    102: "Momen",
    103 : "Shuvo",

}
print(studenId[101])
#print(studenId[108]) # getting error cz of not exit 108 must be use .get function
print(studenId.get(103))
print(studenId.get(107, "non exit"))
print(studenId.get(101, "non exit"))