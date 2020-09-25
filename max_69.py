class Solution:
    def maximum69Number (self, num: int) -> int:
        num_arr = [i for i in str(num)]
        for i in range(len(num_arr)):
            if num_arr[i] == '6':
                num_arr[i] = '9'
                return int(''.join(num_arr))
        return num
