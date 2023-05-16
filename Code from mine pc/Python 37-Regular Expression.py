import re
pattern = r"color"
pattern2= r"col"                        #match (): search first word to find either not match
                          #findall(): feedback the ans as in list

print(re.findall(pattern, "i love green color , orange is mine t.shirt color"))
print(re.findall(pattern2, "i love green color , orange is mine t.shirt color"))
if re.match(pattern, "I love green color, green is every where"):
    print("Match")
else:
    print("Not Match")
if re.search(pattern, "I love green color, green is every where"):
    print("Match")
else:
    print("Not Match")

pattern3 = "country"
text = " i Love My country"
match = re.search(pattern3, text)

if match:
    print(match.start())  #return starting index where matched
    print(match.end())      #return ending index where matched
    print(match.span())     #return starting and ending  index where matched
    #=======================================================================#


pattern4 = "colour"
text2 = "I love green colour , cz it's discribed in our Holy Book about this colour"

text3=re.sub(pattern4, "color", text2, count=2) #replace according to count value
print(text3)
