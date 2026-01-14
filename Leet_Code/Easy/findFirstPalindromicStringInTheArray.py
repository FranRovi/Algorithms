# Leet Code Algo 2108. Find First Palindromic String in the Array

def firstPalindrome(words):
    answer = ""
    is_palindromic = True
    for i in range(len(words)):
        right_idx = len(words[i]) - 1
        for j in range((len(words[i])// 2) +1):
            if words[i][j] == words[i][right_idx - j]:
                is_palindromic = True
                continue
            else:
                is_palindromic = False
                break
        if is_palindromic:
            answer = words[i]
            break
    return answer

print(firstPalindrome(["abc","car","ada","racecar","cool"]))
print(firstPalindrome(["notapalindrome","racecar"]))
print(firstPalindrome(["def","ghi"]))
print(firstPalindrome(["xngla","e","itrn","y","s","pfp","rfd"]))
print(firstPalindrome(["umicrszeaswtfmctwvoogehszwdjrwdcgyxxetbzevxrqphubyqbgpfetguyv","vzdzfwyevkvqhmvqssnvpayihawydzcovzmh","drvqqepesvornphmikbimxennygxisdysssmxjmaaecaqiwdgfxitoopigxauoojsebjmbcrymvpnnfomlkg","vvszfvtykdyfiywxgxmjpcawzdaovbujmexggwczovhspkrdsskxzrpgfaspnbncdspktcyfkkshpyojwwlysizd","epdtgfhgninnwqzztwm","dmhynaogcxyaxsghzjwzyqfuwyinstxoqcdkxeobinpqeplw","ruhxgdrzfyqyqmxclfqosyczqapiizxlzgixdxthhrv","dwcblqnxtrwtqmtqenidhxnifdbmdvobwmcvwjxgbyjzgvrqzlskjbfirauguhyyjhlotuckssrkqzppzbqd","gxdq","paesyowqeguvxozbixjqppeagycjx","glstauwugkidegnllapgzbzchckepmhbameuigsiqywbilwolxuwzzjwzouqknhlkbjzejxtponmkqjlojurxnryxyqy","inyhioiwanafuhsprudtkqztoakxhbmqcmibsxlhycbmqrvtfabsncmiymthcxwkwkq","djknenppuleedpptrfjgqfejcoghnxjlvjalxkyvnujgiiwdbtvgqvgsivkzqcrbfcvooyhqmrlacyiozytmampjwpknrj","zzrpjoogwkdmdxdkdwgwugqtmzryrgtelnvydyqewpdzzptqzvffppgnhhcaiqotmyslntlwjajzuzbawidpxjtyxryg","xmegifttkamzbpjqbghgwdrkvtnuwfmjdmwehdqiyvgpxxlbkcvkemjbmhbyeqyfssytuwaeysvgnidhcgpncxdxxzhrkbvyqfrs","wgljaiyhyfdijjgihseciabfcoqfojhswewpkpartzmaaglvdfifpptycyonigwcgyklapzojivgojcrevugspejmwanolg","oceurgzgvvctgydqexhghwcochhmtoxjugreqfdnsshffngchetrwedhinosdhwlgviohpkjowr","dyl","vjxkcihfmnmmz","aheg","dwsomlqmaqifihkwahvywzqamgominhxfsgrgbgvoiopnikhxonpetelfsguvhxgiujrij","pdrjgfqzyqczpwdsfzypgkmsvnpboutmcffqrwuzkchaufymmczrdwulbvbanungpxqk","eudbizaabgfzqytowifsuovmxmkjgajtliyfycbrkxeaarakapqoihawmdzmglfnglpwqnfd","txdclnfwxevu","kslqrafjshhadqszeljcekrpnpxqgppbnadmzmpufvadcghxqdqmafpbnutifigstxyilmgx","yhhvhyoolv","sjtubggxcla","vydf"]))