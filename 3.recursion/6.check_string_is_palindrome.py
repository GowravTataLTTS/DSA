# check if a string is palindrome
def check_palindrome(string):
    new = list()
    n = len(string) - 1
    while n >= 0:
        new.append(string[n])
        n -= 1
    return list(string) == new


# print(check_palindrome('mom'))

def check_palindrome_two(string):
    i, j = 0, len(string) - 1
    while i > j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


print(check_palindrome_two('malayalam'))


def check_palindrome_recursion(string):
    i = 0
    if string[i] == '':
        return
    return string[i] == check_palindrome_recursion(string[i - 1])


word = 'gowrav'

print(check_palindrome_recursion(string=word))
