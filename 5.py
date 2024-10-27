def palindrome(strng):
    listn = [i.lower() for i in strng if i.isalpha()]
    return listn == listn[::-1]
print(palindrome("A man a plan a canal Panama"))
print(palindrome("Hello"))