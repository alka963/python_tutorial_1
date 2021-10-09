def factorial():
    num = int(input('enter a number'))
    fact = 1
    i = 1
    while(num>0):
        fact = fact * num
        num = num - i
    print(fact)
factorial()