list = [1,2,4,2,3,4]
list1 = []
for x in list:
    if x not in list1:
        list1.append(x)
print(list1)