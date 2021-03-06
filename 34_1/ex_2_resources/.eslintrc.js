module.exports = {
  env: {
    browser: true,
    commonjs: true,
    es2021: true,
  },
  extends: [
    'airbnb-base',
  ],
  parserOptions: {
    ecmaVersion: 12,
  },
  rules: {
    'space-before-function-paren': ['error', {
      anonymous: 'always',
      named: 'always',
      asyncArrow: 'always',
    }],
    'no-console': false,
  },
};
