list = []
temp = 0
n = int(input('how many elements you want to enter...'))
for x in range(n):
    ele = int(input('enter a element'))
    list.append(ele)
    for x in range(0,len(list)):
        for y in range(x + 1,len(list)):
            if list[x] < list[y]:
                temp = list[x]
                list[x] = list[y]
                list[y] = temp
print('The second largest number is ',list[1])
