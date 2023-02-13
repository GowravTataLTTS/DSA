def print_all(n):
    if n > 0:
        print_all(n - 1)
        print(n)


# print_all(13)


def print_all_reverse(n):
    if n > 0:
        print(n)
        print_all_reverse(n - 1)


# print_all_reverse(13)


# sum of all digits from 1 to n
def sum_all(n):
    if n == 1:
        return 1
    return n + sum_all(n - 1)


# print(sum_all(5))

def sum_of_digits(n):
    i = 0
    while n > 0:
        i += n % 10
        n //= 10
    return i


# print(sum_of_digits(4000))

# sum of digits using recursion

def recursion_digit_sum(n):
    if n == 0:
        return 0
    return recursion_digit_sum(n // 10) + n % 10


# print(recursion_digit_sum(4000))


def total_number_of_digits(n):
    i = 0
    while n > 0:
        i += 1
        n //= 10
    return i


# print(total_number_of_digits(n=1000))

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


# print(check_palindrome_two('y'))


def check_palindrome_recursion(string):
    i = 0
    if string[i] == '':
        return
    return string[i] == check_palindrome_recursion(string[i - 1])


word = 'gowrav'

print(check_palindrome_recursion(string=word))
