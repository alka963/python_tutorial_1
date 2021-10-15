num = [9,1,2,90,56,78,35,89]
for x in range(0, len(num)):
    for y in range(x+1, len(num)):
        if num[x] < num[y]:
            num[x],num[y] = num[y],num[x]
print(num)