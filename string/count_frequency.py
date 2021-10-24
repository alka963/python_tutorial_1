str = input('enter string')
str2 = dict()
for x in str:
    if x in str2:
        str2[x] = str2[x] + 1
    else:
        str2[x] = 1
print(str2)