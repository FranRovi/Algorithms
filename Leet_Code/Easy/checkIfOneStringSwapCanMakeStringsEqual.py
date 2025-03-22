# Leet Code Algo 1790. Check if One String Swap Can Make Strings Equal

def areAlmostEqual(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    different_letter_s1 = []
    different_letter_s2 = []
    counter = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            different_letter_s1.append(s1[i])
            different_letter_s2.append(s2[i])
            counter += 1
    different_letter_s1_sorted = sorted(different_letter_s1)
    different_letter_s2_sorted = sorted(different_letter_s2)
    if (different_letter_s1_sorted == different_letter_s2_sorted and counter < 3):
        return True
    return False

print(areAlmostEqual("bank","kanb"))
print(areAlmostEqual("attack","defend"))
print(areAlmostEqual("kelb","kelb"))