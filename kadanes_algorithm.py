def kadanes_algorithm(array):
    max_so_far = []
    max_so_far.append(array[0])
    for i in range(1, len(array)):
        max_so_far.append(max(array[i], array[i]+max_so_far[i-1]))
    return max(max_so_far)

print(kadanes_algorithm([-2,1,-3,4,-1,2,1,-5,4]))

"""
Need to find the max consecutive sum within the array
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""