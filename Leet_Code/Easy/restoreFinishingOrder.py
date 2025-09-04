# Leet Code Algo 3668. Restore Finishing Order

def recoverOrder(order, friends):
    hash_order = {}
    len_friends = len(friends)
    for i in range(len_friends):
        for j in range(len(order)):
            if friends[i] == order[j]:
                hash_order[friends[i]] = j
                break
    sort_dict = dict(sorted(hash_order.items(), key=lambda item: item[1]))
    return list(sort_dict.keys())

print(recoverOrder([3,1,2,5,4],[1,3,4]))
print(recoverOrder([1,4,5,3,2],[2,5]))