even = 0
odd = 0
ctr = 0
while(ctr<5):
    num = int(input('enter {} value'.format(ctr + 1)))
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    ctr = ctr + 1
print('even value: ',even)
print('odd value: ',odd)