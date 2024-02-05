# Leet Code Algo 2347. Best Poker Hand

def bestPokerHand(ranks, suits):
    suitsHash = {}
    ranksHash = {}
    for i in range(len(suits)):
        if suits[i] not in suitsHash:
            suitsHash[suits[i]] = 1
        else:
            suitsHash[suits[i]] += 1
    
    for j in range(len(ranks)):
        if ranks[j] not in ranksHash:
            ranksHash[ranks[j]] = 1
        else:
            ranksHash[ranks[j]] += 1
    sortedranksHash = sorted(ranksHash.items(), key=lambda x:x[1], reverse=True)
    sortedDictByRank = dict(sortedranksHash)
    if len(suitsHash) == 1:
        return "Flush"
    elif list(sortedDictByRank.items())[0][1] >= 3:
        return "Three of a Kind"
    elif list(sortedDictByRank.items())[0][1] == 2:
        return "Pair"
    else:
        return "High Card"
            
print(bestPokerHand([13,2,3,1,9],["a","a","a","a","a"]))  # Flush
print(bestPokerHand([4,4,2,4,4],["d","a","a","b","c"]))  # Three of a Kind
print(bestPokerHand([10,10,2,12,9],["a","b","c","a","d"]))  # Pair 
print(bestPokerHand([9,2,13,1,2],["b","d","d","b","c"]))  # Pair
print(bestPokerHand([5,8,2,11,4],["d","a","d","b","c"]))  # High Card
print(bestPokerHand([10,5,3,5,5],["b","b","d","c","a"]))  # Three of a Kind