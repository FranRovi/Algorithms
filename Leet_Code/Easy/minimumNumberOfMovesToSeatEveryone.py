# Leet Code Algo 2037. Minimum Number of Moves To Seat Everyone.

def minMovesToSeat(seats, students):
    counter = 0
    sorted_seats = sorted(seats)
    sorted_students = sorted(students)
    for i in range(len(seats)):
        counter += abs(sorted_seats[i] - sorted_students[i])
    return counter

print(minMovesToSeat([3,1,5],[2,7,4]))
print(minMovesToSeat([4,1,5,9],[1,3,2,6]))
print(minMovesToSeat([2,2,6,6],[1,3,2,6]))