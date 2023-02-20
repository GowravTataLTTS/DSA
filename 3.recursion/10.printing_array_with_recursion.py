arra = [1, 2, 3, 4]

size = len(arra)


def array_recursion(size, arra):
    while size > 0:
        print(arra[size - 1])
        size -= 1
        # array_recursion(size - 1, arra)


print(array_recursion(size, arra))
