# def can_sum(target, numbers):
#     "Exponential time complexity Brute force approach O(n^m). n==len(array) and m is target"
#     if target == 0:
#         return True
#     if target < 0:
#         return False

#     for num in numbers:
#         remainder = target - num
#         if can_sum(remainder, numbers):
#             return True
#     return False


"""
Memoized solution
Time: O(m*n)
Space: O(n)
"""
def can_sum(target, numbers, memo={}):
    "Exponential time complexity Brute force approach O(n^m). n==len(array) and m is target"
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for num in numbers:
        remainder = target - num
        if can_sum(remainder, numbers):
            memo[target] = True
            return True
    memo[target] = False
    return False

print(can_sum(300, [7, 14]))
# print(can_sum(6, [2, 3, 3]))