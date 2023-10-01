# Step1 : tail
# Step2 : body
# def isPalindrome(s):
#     print(s == s[::-1])
#     return s == s[::-1]
#
#
# # Driver code
# s = "malayalam"
# ans = isPalindrome(s)
#
# if ans:
#     print("Yes")
# else:
#     print("No")

def isPalindrome(s):
    print(s)
    print(len(s))
    if len(s) == 1:
        return True
    if s[0] == s[-1]:
        return True
    else:
        return False

    isPalindrome(s[1:len(s) - 2])

print('This is Palindrome? ', isPalindrome('abaa'))