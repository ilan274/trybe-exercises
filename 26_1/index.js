const readLineSync = require('readline-sync');
const inquerer = require("inquirer");
const { calculateAnswer } = require('./calculateAnswer');

const imc = () => {
  const weight = readLineSync.questionFloat("Please enter your weight: ");
  const height = readLineSync.questionFloat("Please enter your height (in meters): ");
  const answer = (weight / (height ** 2)).toFixed(2);
  calculateAnswer(answer);
};

const imcInq = () => {
  const numRegex = new RegExp(/[0-9]/);
  inquerer.prompt([
    {
      type: 'input',
      name: 'weight',
      message: "Please enter your weight:",
      validate: input => {
        if (numRegex.test(input)) return true;
        return "Please enter a valid number";
      }
    },
    {
      type: "input",
      name: 'height',
      message: "Please enter your height:",
      validate: input => {
        if (numRegex.test(input)) return true;
        return "Please enter a valid number";
      }
    },
  ])
    .then(resposta => {
      const answer = (resposta.weight / (resposta.height ** 2)).toFixed(2);
      calculateAnswer(answer);
    });
};
