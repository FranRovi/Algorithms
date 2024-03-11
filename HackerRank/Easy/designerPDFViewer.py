# Hacker Rank Algo Designer PDF Viewer

def designerPDFViewer(h, word):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    hashLetters = {}
    for i in range(len(alphabet)):
        hashLetters[alphabet[i]] = h[i]
    # hashLetters = {
    #     'a': h[0],
    #     'b': h[1],
    #     'c': h[2],
    #     'd': h[3],
    #     'e': h[4],
    #     'f': h[5],
    #     'g': h[6],
    #     'h': h[7],
    #     'i': h[8],
    #     'j': h[9],
    #     'k': h[10],
    #     'l': h[11],
    #     'm': h[12],
    #     'n': h[13],
    #     'o': h[14],
    #     'p': h[15],
    #     'q': h[16],
    #     'r': h[17],
    #     's': h[18],
    #     't': h[19],
    #     'u': h[20],
    #     'v': h[21],
    #     'w': h[22],
    #     'x': h[23],
    #     'y': h[24],
    #     'z': h[25]    
    # }
    max = int(hashLetters[word[0]])
    for j in range(1, len(word)):
        if hashLetters[word[j]] > max:
            max = hashLetters[word[j]]
    return max * len(word)
print(designerPDFViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],'abc'))
print(designerPDFViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7],'zaba'))