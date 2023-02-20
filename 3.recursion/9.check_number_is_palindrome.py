def check_number_palindrome(n):
    s = n
    j = ''
    while n > 0:
        j += str(n % 10)
        n = n // 10
    return s == int(j)


print(check_number_palindrome(101))
