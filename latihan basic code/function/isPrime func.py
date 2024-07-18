def isPrime(x):
    test=True
    for i in range(2,x):
        if (x%i) == 0:
            test=False
            break
    if test:
        return print("it's Prime...")
    else:
        return print("isn't Prime :(")
        
isPrime(25)