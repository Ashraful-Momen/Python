def square(x):
    return x*x

num=[1,2,3,4]

result = list(map(square, num)) # not use f "()" bracket
print(result)

#=========== filter (f(),list)======== if the condition not matchi in list that's will remove

num.append(5)
num.append(6)
print(num)

ans = list(filter(lambda x : x%2==0, num))

print(ans)