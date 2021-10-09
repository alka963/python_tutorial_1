def prime():
    i = 1
    ctr = 0
    for x in range(1,num+1):
        if (num % x == 0):
            ctr = ctr + 1
    if ctr == 2:
        print('prime no')
    else:
        print('not prime number')
num = int(input('enter number'))
prime()
