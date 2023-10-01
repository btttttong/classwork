import random
# def climbStairs(n):
#     if n <= 2:
#         return n
#     return climbStairs(n - 1) + climbStairs(n - 2)
#
# print("Number of ways = ")
# print(climbStairs(44))

# Dynamic Programming
def climbStairs(n):
    memo = [1, 1]
    for i in range(2, n + 1):
        current_val = memo[-1] + memo[-2]
        memo.append(current_val)
    return memo[-1]

print(climbStairs(44))


