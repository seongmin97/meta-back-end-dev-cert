## Intro
- what is fullstack
  - front-end, back-end, database stack
  - devops skills
  - version control
- N-tier architecture
  - presentation, application, data tiers

## Front-end tech
- HTML
- semantic tags
- form validation
  - client side: as soon as they are typed into the form. Done by web browser or javascripts code.
  - server side: more complex check
- CSS web layout
  - flexbox : one dimensional
  - grid: two dimensinals
- Widely used selectors
  - attribute selector
  - nth-of-type and nth-child selectors
  - start selector (*)
  - group selector
- Document flow: block vs inline
- basic flexbox
  - search bar
  - navigation bar
  - image gallery
- CSS grid
  - px:pixel
  - fr:fraction
  - repeat function
  - minmax function
- All selectors and their specificity
- Pseudo-class
  - User action state Pseudo-classes have an effect while a user is actively engaging with an HTML element. 
    - The active pseudo-class changes the properties of an element when the state of that element is active like the appearance of a button.
    - You can use the hover Pseudo-class to target an item while a user is hovering over it. 
- Pseudo-elements
  - ::first-letter
  - ::first-line
  - ::selection
  - ::marker
  - ::before, ::after

- JavaScript
  - It is used almost every websites.
- programming in javascript
  - react
  - legancy code
- variables
```JavaScript
var person = "John"
person;
//John

console.log("Hello", person)
// hello John

=================================================
var petDog = "Rex"
var petCat = "Peper"
console.log("My pet dog's name is: " , petDog)
console.log("My pet cat's name is: ", petCat)

var catSound = "purr"
var dogSound = "woof"
console.log(petDog, "syas", dogSound)
console.log(petCat, "says", catSound)

catSound = "meow"
console.log(petCat, "now says", catSound)

// My pet dog's name is:  Rex
// My pet cat's name is:  Peper
// Rex syas woof
// Peper says purr
// Peper now says meow
```

- Datatype
- Operators
- Nummbers
- Strings
- Boolean
  - 100 == "100" : true
  - 100 === "100" : false, because of the type
  - 1 !== "1" : false, because of the type
- JavaScript selectors
- scoping with vat let and const
  - global and local scope
  - let and const are strict 
    - can't be used before it is declared
    - variable can't be redeclared
    - it's scoped to the block
  - var in ES5, let/const in ES6
- functions
  - parameters: function addtwonums(a,b){ ... }
  - arguments: addtwonums(2,2)
- JS DOM manipulation
  - DOM: document object model. The DOM is a structured representation of a webpage, allowing developers to interact with and manipulate the content and structure of the page dynamically.
- Event handling


## The full stack using Django
- Configure Django to connect mysql
```sql
-- create new user
CREATE USER 'coursera'@'localhost' IDENTIFIED BY 'coursera';

create database menu_items;

GRANT ALL PRIVILEGES ON menu_items.* TO 'coursera'@'localhost';

FLUSH PRIVILEGES;
exit;
```
- Form and model forms
- Fetching data with js
- Querying APIs using JavaScript
```JavaScript
// e.g. POST method
const payload = {
    "title": "Ambrosia Ice cream",
    "price": 5.00,
    "inventory": 100
}
const endpoint = 'http://127.0.0.1:8000/api/menu-items'
fetch(endpoint,
    {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })


```

## Production env