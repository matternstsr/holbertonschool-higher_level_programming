#!/usr/bin/node

// Get command-line arguments excluding the first two (node executable and script file)
const args = process.argv.slice(2);
// Check if there are less than or equal to 1 argument, if true, print 0 and exit
if (args.length <= 1) {
  console.log(0);
} else {
  // Convert command-line arguments to an array of numbers
  const numbers = args.map(Number);
  // Find unique numbers by converting the array to a Set and back to an array
  const findUniqueNumbers = Array.from(new Set(numbers));
  // Sort the unique numbers in descending order
  const allSortedNumbers = findUniqueNumbers.sort((a, b) => b - a);
  // Print the second largest number
  console.log(allSortedNumbers[1]);
}