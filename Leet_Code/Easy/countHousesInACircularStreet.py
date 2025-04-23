# Leet Code Algo 2728. Count Houses in a Circular Street

def houseCount(street, k):
    idx = 0
    while idx <= k:
        street.closeDoor()
        street.moveRight()
        idx += 1 
    counter = 0
    idx = 0
    while idx <= k:
        if idx == 0:
            street.openDoor()
            street.moveRight()
        else:
            if street.isDoorOpen():
                return counter
            else:
                street.moveRight()
        counter += 1
        idx += 1
