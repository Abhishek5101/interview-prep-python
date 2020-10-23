# "aaabbaa" ---> [('a', 3), ('b', 2), ('a', 2)]

def compression(string):
    solution = []
    count = 1
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            solution.append((string[i-1], count))
            count = 1
        else:
            count += 1
    solution.append((string[-1], count))
    return solution

print(compression("aaabbaac"))