# Leet Code Algo 1344. Angle Between Hands of a Clock.

def angleClock(hour, minutes):
    diff_angles = abs(hour * 30 - minutes * 5.5)
    if diff_angles > 180:
        return 360 - diff_angles
    return diff_angles

print(angleClock(12, 30))
print(angleClock(3, 30))
print(angleClock(3, 15))
