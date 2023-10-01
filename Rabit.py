# def rabit(n):
#     if n == 1 or n == 2:
#         return 1
#     if n == 0:
#         return 0
#     return rabit(n-1) + rabit(n-2)
#
# print(rabit(12))


def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 1

    # Check if n is 1,2
    # it will return 1
    elif n < 3:
        return n

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

# Driver Program
print(Fibonacci(12))
