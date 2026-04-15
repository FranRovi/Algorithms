# Leet Code Algo 3894. Traffic Signal Color

def trafficSignal(timer):
    if timer > 30 and timer <= 90:
        return "Red"
    elif timer == 30:
        return "Orange"
    elif timer == 0:
        return "Green"
    else:
        return "Invalid"

print(trafficSignal(60))
print(trafficSignal(5))