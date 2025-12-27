# Leet Code Algo 2483. Minimum Penalty for a Shop

def bestClosingTime(customers):
    visit_arr = []
    counter = 0
    max_counter = [0, 0]
    len_cust = len(customers)
    for i in range(len_cust):
        if customers[i] == "Y":
            counter += 1
            visit_arr.append(i)
            if counter > max_counter[0]:
                max_counter[0] = counter
                max_counter[1] = i + 1
        else:
            counter -= 1
    if len(visit_arr) == len_cust:
        return len_cust 
    elif len(visit_arr) == 0:
        return 0
    else:
        return max_counter[1]
    
print(bestClosingTime("YYNY"))
print(bestClosingTime("NNNNN"))
print(bestClosingTime("YYYY"))