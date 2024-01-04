# Leet Code Algo 2951. Find The Peaks

def findThePeaks(mountain):
    peakIndeces = []
    for i in range(1, len(mountain) - 1):
        if (mountain[i] > mountain [i - 1] and 
            mountain[i] > mountain [i + 1]):
                peakIndeces.append(i)
    return peakIndeces

print(findThePeaks([2,4,4]))
print(findThePeaks([1,4,3,8,5]))