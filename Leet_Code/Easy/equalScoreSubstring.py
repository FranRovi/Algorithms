# Leet Code Algo 3707. Equal Score Substring

def scoreBalance(s):
    hash_score = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
    arr_val = []
    for c in s:
        arr_val.append(hash_score[c])

    left_idx = 0
    right_idx = len(arr_val) - 1
    left_sum = 0 
    right_sum = 0

    len_arr_val = len(arr_val)
    for i in range(len_arr_val):
        if left_sum >= right_sum:
            right_sum += arr_val[right_idx]
            right_idx -= 1
        else:
            left_sum += arr_val[left_idx]
            left_idx += 1
    return True if left_sum == right_sum else False

print(scoreBalance("adbc"))
print(scoreBalance("bace"))