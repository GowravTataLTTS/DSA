def countDigits(n):
    i = 0
    while n > 0:
        i += 1
        n //= 10
    return i


