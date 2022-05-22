
# def twoSum(nums, target):
#     hash = {}
#     i = 0
#     while i < len(nums):
#         num = target - nums[i]
#         if num in hash.keys():
#             return [hash[num], i]
#         else:
#             hash[nums[i]] = i


# testRes = twoSum([1,2,3], 4)
a = str(0)
b = str(1)
dict = dict(a=1, b=2)
if "a" in dict.keys():
    print("a in dict")
    print(dict["a"])
else:
    print("a not in dict")
    print('a' in dict.keys())


def twoSum(nums, target):
    hash = {}
    for i, num in enumerate(nums):
        if hash.get(target - num) is not None:
            return [hash.get(target - num), i]
        hash[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0): return False
    y = 0
    while x > y:
        y = x % 10 + y * 10
        x = x // 10
    return x == y or x == y // 10
    

print(isPalindrome(121))