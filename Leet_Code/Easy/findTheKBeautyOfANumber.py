# Leet Code Algo 2269. Find the K-Beauty of a Number

def divisorSubstrings(num, k):
    num_arr = list(str(num))
    temp_num_str = num_arr[:k]
    possible_divisors = [int("".join(temp_num_str))]
    for i in range(k, len(num_arr)):
        temp_num_str.append(num_arr[i])
        temp_num_str.pop(0)
        possible_divisors.append(int("".join(temp_num_str)))
    counter = 0
    for n in possible_divisors:
        if n == 0:
            continue
        else:
            if num % n == 0:
                counter += 1
    return counter

print(divisorSubstrings(240, 2))
print(divisorSubstrings(430043, 2))