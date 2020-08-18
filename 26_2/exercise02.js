/*
Exercise 2: Now, take the function from exercise 1 and refactor it to async / await.
  Your function has to work exactly like exercise 1, but you cannot use any .then in your code.
  For each exercise below, write the script first using callbacks, then promises, and lastly, async / await.
*/

async function errorsTreatment(x, y, z) {
  const params = [x, y, z];
  const nan = params.some(param => typeof param !== 'number');
  if (nan) return new Error('Enter numbers only');
  const mult = (x + y) * z;
  if (mult < 50) return new Error('Very low value');
  return ((x + y) * z);
};

const answer = errorsTreatment(2, '200', 2);
console.log(answer);
