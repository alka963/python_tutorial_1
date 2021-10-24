str = input('enter a string')
str2 = ' '
for x in str :
    if x not in str2:
        str2 = str2 + x
print(str2)
