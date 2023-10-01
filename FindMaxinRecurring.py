# step1: Tail
# step2: Body

list = [3, 4, 5, 1, 2, 1]
tmp = []

def devide_arr(arr):
    if len(arr) == 1:
        return arr[0]
    last = arr[::-1]
    rest = arr[:len(arr)-2]
    if last > devide_arr(rest):
        return last
    else:
        return devide_arr()

devide_arr(list)