def dup(listn):
    lstn = listn
    for i in range(len(lstn)-1):
        if lstn[:i+1].count(lstn[i]) > 1:
            listn.pop(i)
    return listn      

print(dup(['a', 'b', 'a', 'c'] ))
print(dup([1, 2, 2, 3, 4, 4, 5]))