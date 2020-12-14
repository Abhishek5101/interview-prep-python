"""
Time: O(n*m*m)
Space: O(m*m)
"""
# def best_sum(target, numbers):
#     if target == 0: return []
#     if target < 0: return None

#     shortest = None

#     for num in numbers:
#         remainder = target - num
#         remainder_result = best_sum(remainder, numbers)
#         if remainder_result is not None:
#             combination = remainder_result + [num]
#             if shortest is None or len(combination) < len(shortest):
#                 shortest = combination
#     return shortest

# print(best_sum(8, [1,8,2]))
"""
Memoization
Time: O(n*m*m)
Space: O(m*m)
"""

def best_sum(target, numbers, memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    shortest = None

    for num in numbers:
        remainder = target - num
        remainder_result = best_sum(remainder, numbers, memo)
        if remainder_result is not None:
            combination = remainder_result + [num]
            if shortest is None or len(combination) < len(shortest):
                shortest = combination
    memo[target] = shortest
    return shortest

print(best_sum(686, [7, 14]))