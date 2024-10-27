def eureka(a,b):
    listn = []
    for i in range(a,b):
        sum = 0
        for z in str(i):
            sum += int(z) ** (str(i).index(z) + 1)
        if sum == i:
            listn.append(i)
    return listn
print(eureka(1,100))