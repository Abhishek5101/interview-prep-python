# def monotone_increasing(num):
#     while True:
#         if is_increasing(num):
#             return num
#         else:
#             num -= 1


# def is_increasing(num):
#     str_num = str(num)
#     for i in range(len(str_num)-1):
#         if int(str_num[i + 1]) < int(str_num[i]):
#             return False
#     return True


# def is_increasing_leetcode(num):
#     for i in range(len(str(num))-1):
#         if num[i + 1] < num[i]:
#             return False
#     return True

# print(is_increasing_leetcode(10))


def monotoneIncreasingDigits(N: int) -> int:
    pivot, s = 0, list(str(N))
    for i in range(1,len(s)):
        if s[i-1] < s[i]:
            # print(s[i-1], s[i])
            pivot = i
            # print(pivot)
        elif s[i-1] > s[i]:
            print(s[i-1], s[i])
            s[pivot] = str(int(s[pivot])-1)
            print(s[pivot])
            s[pivot+1:] = '9'*(len(s)-pivot-1)
            print(s[pivot+1:])
            break
    return int(''.join(s))

print(monotoneIncreasingDigits(322))