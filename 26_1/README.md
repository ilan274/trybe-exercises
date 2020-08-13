### Exercise requirements

The script should calculate a person's BMI and display it on the screen. Create a new package called calcula-imc, and use the npm start script to run our index.js file. Continue using the readline-sync package to collect user data. The formula for calculating BMI is weight / height².

Note: Remember that weight and height are not always integers and therefore we cannot use the questionInt function in the readline-sync package. However, the same package has a function to treat numbers with decimal places. Find this function in the readline-sync documentation and don't forget to use toFixed (2) in decimal numbers!

Tip: To use npm start, remember to configure your package.json, adding a start to your scripts: "node index.js", for example. In this example, index.js represents the main file for your package.json.

Now, modify the script above so that it tells you if the person, whose BMI was calculated, has some level of obesity. Consider the following table to find out what situation should be presented for each result:

BMI Situation
Under 18.5 Underweight (thinness)
Between 18.5 and 24.9 Normal weight
Between 25.0 and 29.9 Overweight (overweight)
Between 30.0 and 34.9 Obesity grade I
Between 35.0 and 39.9 Obesity grade II
40.0 and above Obesity grades III and IV
Finally, modify the script so that it uses the inquirer package to request information from the user at the terminal. To understand how to use the inquirer, consult the documentation on the npm website. Besides, you may need to recall what we already learned about Promises in another class.

Note: Use the validate property of the inquirer's questions to verify that the values ​​entered are valid numbers.