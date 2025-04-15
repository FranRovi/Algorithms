# Leet Code Algo 3498. Reverse Degree of a String

def reverseDegree(s):
    hash_letters = {
        'a':26,'b':25,'c':24,'d':23,'e':22,'f':21,'g':20,'h':19,
        'i':18,'j':17,'k':16,'l':15,'m':14,'n':13,'o':12,'p':11,
        'q':10,'r':9,'s':8,'t':7,'u':6,'v':5,'w':4,'x':3,
        'y':2,'z':1        
    }
    total_sum = 0
    for i in range(len(s)):
        total_sum += (i+1) * hash_letters[s[i]]
    return total_sum

print(reverseDegree("abc"))
print(reverseDegree("zaza"))