from typing import List

def return_digit(num):
    res = []
    test = str(num)
    for i in num:
        res.append(int(i))
    return res


print(return_digit('1000'))

print([int(x) for x in str('123')])


def range_i(n: int) -> List[int]:
    res = []
    while n != 0:
        res.insert(0, n % 10)
        n = n // 10
    return res
print(range_i(123))

def range_n(n: int) -> List[int]:
    res = []
    while n != 0:
        res.append(n % 10)
        n = n // 10
    return sorted(res)
print(range_n(123))


