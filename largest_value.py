high = 0
ctr = 0
while(ctr<=10):
    num = int(input('enter {} value'.format(ctr + 1)))
    if num > high:
        high = num
    ctr = ctr + 1
print('highest value',high)