# def sortArrayByParity(nums):
#     ret = []
#     for i in nums:
#         print(i)
#         if not len(ret):
#             ret.append(i)
#         else:
#             print ('mod',i%2)
#             if i % 2 == 0 or i == 0:
#                 ret.insert(0, i)
#             else:
#                 ret.append(i)
#
#         print(ret)
#     return ret
# print(sortArrayByParity([0,1]))

def sortArrayByParity(nums):
    #มี pointer สำหรับชี้ว่าตอนนี้เราอยู่ที่ index ไหน ซ้าย - ขวา
    left = 0
    right = len(nums)-1
    #ถ้าตน.ซ้าย < ขวา = ขยับไปเรื่อย
    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 == 1:
            right -= 1
        else:
            nums[left],nums[right] = nums[right],nums[left]
    return nums


print(sortArrayByParity([0, 1]))