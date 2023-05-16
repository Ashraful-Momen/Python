 
try: 
     list = [10,0,3]
     ans = list[0]/list[3] # ZeroDivisionError: division by zero
     print(ans) # after error this line is not exectuded


except (ZeroDivisionError,IndexError) as all :
    print("Dividing by zero is not possible or index of range")




finally: 
    print("Must be print this line if those error isn't handle yet!")
    print(" ")
'''except ZeroDivisionError :
    print("Dividing by zero is not possible")
except IndexError :
    print("list index out of range")'''
try: 
    def voter(age):
        if age<18:                      # raise: if the condition is false the executed it
                                    # if the condition is true

            raise ValueError("your age is not valid for voting")
        return "you are valid for voting"
except ValueError as e:
    print("value error is printing in Here") 
print(voter(17))
    



