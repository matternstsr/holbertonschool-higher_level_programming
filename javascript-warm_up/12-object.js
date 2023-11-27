#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
// Your code here
const updatedObject = { ...myObject, value: 89 };
console.log(updatedObject);
