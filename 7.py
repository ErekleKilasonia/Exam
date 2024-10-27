def fibonacci(x):
    listn = [0,1]
    counter = 1
    if x == 1:
        return [0]
    if  x == 0:
        return []
    while len(listn) < x:
        listn.append(listn[counter] + listn[counter-1])
        counter += 1
    
    return listn
print(fibonacci(2))
print(fibonacci(7))

