def find_gcd_number(a, b):
    maxer = 1
    s = b % a
    while s > 1:
        if a % s == 0 and b % s == 0:
            maxer = s
            break
        s -= 1
    return maxer


print(find_gcd_number(42, 60))
