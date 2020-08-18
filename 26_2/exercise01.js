/*
Exercise 1: Create a function that returns a promise:
  This function must receive 3 parameters, handling the error if any of the parameters is not a number.
  If any of the parameters are not of the Number type, reject the promise and print the phrase "Enter numbers only" on the screen.
  If all parameters are of type Number, you must add the first two.
  Then take the sum result and multiply it by the third parameter and if it is less than 50, reject the promise with the message "Value too low". 
  Otherwise, accept the promise by printing the result of the multiplication on the screen.
*/

const errorsTreatment = (par1, par2, par3) => {
  return new Promise((resolve, reject) => {
    const paramList = [par1, par2, par3];
    paramList.forEach(par => {
      (typeof par) != 'number' && reject(
        new Error('Enter numbers only')
      );
    });
    const sumFirstTwo = par1 + par2;
    const multiply = sumFirstTwo * par3;
    multiply < 50 && reject('Very low value');
    resolve(multiply);
  });
};

errorsTreatment(10, 10, 3)
  .then(val => console.log(val))
  .catch(err => console.log(err));
