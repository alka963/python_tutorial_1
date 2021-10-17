num = [1,2,7,89,98,89,4,6,46]
num2 = dict()
for x in num:
    if x in num2:
        num2[x] = num2[x] + 1
    else:
        num2[x] = 1
print(num2)
