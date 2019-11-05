typeof true;
typeof false;
// boolean

// 확실히 없다
typeof null;
// object

// 모르겠다
typeof undefined;
// undefined

typeof 'asdf'; // string
typeof 1; // number
typeof 1.1; // number
typeof Infinity; // number
typeof NaN; // number

typeof [1,2]; // object
typeof {a:1, b:2}; // object

typeof function () {}; // function