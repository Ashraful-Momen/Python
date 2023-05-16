def sum(*num):
    add=0
    for x in num:
        add=add+x
        return add # return in under the loop: that why print 10
                    #for debugging tap to execute line staringof f(), shift+f9,f7

print(sum(10,20))