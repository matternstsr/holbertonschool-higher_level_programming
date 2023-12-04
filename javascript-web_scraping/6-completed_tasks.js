#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

// Checking if the API URL is provided
if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <api-url>'); process.exit(1);
}

// Making a GET request to the specified API URL
request.get(apiUrl, (error, response, body) => {
  if (error) { console.error(error); process.exit(1); }

  // Parsing the JSON response
  const todos = JSON.parse(body);

  // Creating an object to store the count of completed tasks per user
  const completedTasksByUser = {};

  // Going through the todo's and count completedtasksbyuser
  todos.forEach((todo) => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) { completedTasksByUser[todo.userId]++; } else { completedTasksByUser[todo.userId] = 1; }
    }
  });

  // Print the results
  console.log(completedTasksByUser);
});
