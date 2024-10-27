def snake_case(x):
    if type(x) is int:
        return str(x)
    word = ""
    for i in x:
        if i.isupper():
            word += "_" + i.lower()
        else:
            if i != " ":
                word += i
    if word[0] == "_":
        return word[1:]
    return word
print(snake_case("TestController"))
print(snake_case("MoviesAndBooks"))
print(snake_case("App7 Test" ))
print(snake_case(1))