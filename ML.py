def is_palindrome(s):
    x1=[]
    x2=[]
    for i in s:
        x1.append(i)
    for i in reversed(s):
        x2.append(i)
    if x1 == x2:
        return True
    else:
        return False


string1 = "radar"
result1 = is_palindrome(string1)
print(result1)

string2 = "Python"
result2 = is_palindrome(string2)
print(result2)
