import re

pattern1 = "col.r"
text1 = "color "
if re.match(pattern1, text1):
    print("Match-1")

    #is testing colour and colour
pattern2 = "^colo..r$"  #staring ^colo **  r $ <=ending

if re.match(pattern2, "coloaar"):
    print("Match-2")

pattern3 = "a*"   #* = (0 or more ) )
if re.match(pattern3, "color"):
    print("Match-3")

pattern4 = "a+"   #* = (1 or more ) )
if re.match(pattern4, "aaaaacolor"):
    print("Match-4")

pattern5 = "(ab)*"   #* = (0 or more ) )
if re.match(pattern5, "aaaaacolor"):
    print("Match-5")

pattern6 = "ice(-)?cream"   #- = (0 or more ) )
if re.match(pattern6, "icecream"): #if "-' exit or nonexit match-6 printed
    print("Match-6")

pattern7 = "a{1,3}$"
if re.match(pattern7, "aaa"):
    print("Match-7")

pattern8 = "[aeiou]"  #if any latter get in string of [] then matched
if re.match(pattern8, "aaa"):
    print("Match-8")

pattern9 = "[A-Z][a-z][0-9]" #must be mantian the sequence [A][a][0-9]
if re.match(pattern9, "Aa9"):
    print("Match-9")