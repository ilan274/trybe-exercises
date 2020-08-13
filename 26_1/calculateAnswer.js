const calculateAnswer = answer => {
  if (answer < 18.5) {
    return console.log("Underweight: %s", answer);
  } else if (answer >= 18.5 && answer <= 24.9) {
    return console.log("Normal weight: %s", answer);
  } else if (answer >= 25 && answer <= 29.9) {
    return console.log("Above weight: %s", answer);
  } else if (answer >= 30 && answer <= 34.9) {
    return console.log("Grade I obesity: %s", answer);
  } else if (answer >= 35 && answer <= 39.9) {
    return console.log("Grade II obesity: %s", answer);
  } else {
    return console.log("Grade III and IV obesity: %s", answer);
  }
};

module.exports = { calculateAnswer };