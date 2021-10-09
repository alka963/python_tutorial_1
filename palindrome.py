def palindrome(num):
    rev = 0
    temp = num
    while(num>0):
        rev = (rev * 10)+ num % 10
        num = num//10
    if rev == temp:
        print('palindrome')
    else:
        print(' not palindrome')
num = int(input('enter a number'))
palindrome(num)