# Leet Code 824.Goat Latin

def goatLatin(sentence):
    answer = ''
    counter = 1
    arrWords = sentence.split(" ")
    for i in range(len(arrWords)):
        if arrWords[i][0].lower() in {"a", "e", "i", "o", "u"}:
            answer += arrWords[i][:] + 'ma' + counter * "a" + " "
        else:
            temp = arrWords[i][0]
            answer += arrWords[i][1:] + temp + 'ma' + counter * "a" + " "
        counter += 1
    answer = answer.rstrip()
    return answer
    
print(goatLatin("I speak Goat Latin"))
print(goatLatin("The quick brown fox jumped over the lazy dog"))

        
        