#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const filtertocount = list.filter(element => element === searchElement); return filtertocount.length;
};
// implementation of the nbOccurences function that returns the number of occurrences of a given element in a list.
// nbOccurences that takes a list and a search element as arguments. It uses the filter method to create a new array
// containing only the elements equal to the search element, and then returns the length of that array, which represents
// the number of occurrences.
