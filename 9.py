def prime_time(x):
    listn = []
    for i in range(2,x+1):
        if prime(i):
            listn.append(i)
    return listn

def prime(num):
    for z in range(2,num):
        if num % z == 0:
            return False
    return True


print(prime_time(10))
