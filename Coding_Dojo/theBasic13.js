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