# Leet Code Algo 2960. Count Tested Devices After Test Operations

def countTestedDevices(batteryPercentages):
    counter = 0
    for i in range(len(batteryPercentages)):
        if batteryPercentages[i] > 0:
            counter += 1
            for j in range(i+1, len(batteryPercentages)):
                if batteryPercentages[j] > 0:
                    batteryPercentages[j] -= 1    
    return counter

print(countTestedDevices([1,1,2,1,3]))
print(countTestedDevices([0,1,2]))