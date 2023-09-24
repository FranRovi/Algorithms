def averageSalary(salary):
    print(salary)
    min = salary[0]
    posMin = 0
    max = salary[0]
    posMax = 0
    totalSum = 0
    
    for i in range(len(salary)):
        if (min > salary[i]):
            min = salary[i]
            posMin = i
        if (max < salary[i]):
            max = salary[i]
            posMax = i
    
    tempMax = salary[posMax]
    if (salary[posMin] == salary[len(salary) - 1]):
        posMin = posMax
    salary[posMax] = salary[len(salary) - 1]
    salary[len(salary) - 1] = tempMax

    tempMin = salary[posMin]
    salary[posMin] = salary[len(salary) - 2]
    salary[len(salary) - 2] = tempMin
      
    for j in range (len(salary) - 2):
        totalSum += salary[j]
    return(totalSum/ (len(salary) -2))
    
print(averageSalary([4000, 3000, 1000, 2000]))
print(averageSalary([1000, 2000, 3000]))
print(averageSalary([7000, 2000, 1000, 4000, 9000, 3000]))  
print(averageSalary([6000, 5000, 4000, 3000, 2000, 1000]))  
            
        