// # Algorithm 1
// Print all the integers from 1 to 255

for (i=1;i<256;i++){
    console.log(i)
}

// # Algorithm 2
// Print integers from 0 to 255, and with each integer print the sum so far.
var totalSum = 0;
// for (i=0;i<256;i++){
for (i=0;i<6;i++){
    totalSum = i + totalSum
    console.log("Current value: " + i + " Total Sum: " + totalSum)
}

// # Algorithm 3
// Given an array, find and print its largest element.
function findAndPrintMax(givenArr){
    max = givenArr[0];
    for(i=1;i<givenArr.length;i++) {
        if (givenArr[i] > max){
            max = givenArr[i]
        }
    }
    console.log("Max number in array is: " + max) 
}
findAndPrintMax([1,2,3,4,5]);
findAndPrintMax([5,6,4,3,2]);
findAndPrintMax([5,7,8,4,6]);

// # Algorithm 4
// Create an array with all the odd integers between 1 and 225 (inclusive).
var oddArr = [];
for (i=1;i<256;i=i+2){
    oddArr.push(i);
}
console.log(oddArr);

// # Algorithm 5
// Given an array and a value Y, count and print the number of array values greater than Y.
function greaterThanY(givenArr, value){
    var numsGreaterThanY = 0;
    for(i=0;i<givenArr.length;i++) {
        if (givenArr[i] > value){
            numsGreaterThanY++
        }
    }
    console.log("Numbers greater than the given value: " + numsGreaterThanY) 
}

greaterThanY([1,2,3,4,5], 1);
greaterThanY([5,6,4,3,2], 3);
greaterThanY([5,7,8,4,6], 6);
