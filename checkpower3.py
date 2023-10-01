def power_three(num):
    print(num)
    if num == 0:
        return False
    if num == 1:
        return True
    if num % 3 == 0:
        return power_three(num//3)

ans = power_three(8)
print(ans)


    