# Hacker Rank Algo. Jim and the Orders

def jimOrders(orders):
    hash_orders = {}
    for i in range(len(orders)):
        if orders[i][0] + orders[i][1]  not in hash_orders:
            hash_orders[orders[i][0] + orders[i][1]] = [i + 1]
        else:
            hash_orders[orders[i][0] + orders[i][1]].append(i + 1)
    sorted_hash_orders_tuple = sorted(hash_orders.items())
    sorted_dict = dict(sorted_hash_orders_tuple)
    customer_arr = list(sorted_dict.values())
    answer = []
    for j in range(len(customer_arr)):
        for k in range(len(customer_arr[j])):
            answer.append(customer_arr[j][k])
    return answer

print(jimOrders([[1,1],[1,2],[1,3]]))
print(jimOrders([[8,1],[4,2],[5,6],[3,1],[4,3]]))    
print(jimOrders([[1,1],[1,1]]))   