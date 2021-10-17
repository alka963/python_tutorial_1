list = [56,3,4,9,8,4,5]
temp = 0
for x in range(0,len(list)):
    for y in range(x + 1,len(list)):
        if list[x] > list[y]:
            temp = list[x]
            list[x] = list[y]
            list[y] = temp
print('second smallest number is ',list[1])