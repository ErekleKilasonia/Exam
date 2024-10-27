def order(strng):
    listn = strng.split()
    my_dict = {}
    for i in listn:
        counter =0
        for z in i:
            if z.isdigit():
                my_dict[i.replace(z,"")] = int(z)
                counter += 1
        if counter == 0:
            my_dict[i] = len(listn)

    listn = []
    for i in my_dict:
        listn.append(i)

    for i in listn:
        for x in listn:
            if my_dict[i] < my_dict[x]:
                listn[listn.index(i)],listn[listn.index(x)] = listn[listn.index(x)],listn[listn.index(i)]
    return " ".join(listn)

print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r people g3ood th5e the2"))