## Getting start

## Basic programming
- Exceptions
- File handling

## Programming paradigm
- map() and filter()
- Comprehensions in Python are a way to create a new sequence from an already existing sequence.
  - List comprehension: `[ <expression> for x in <sequence> if <condition>] `
  - Dictionary comprehension: `dict = { key:value for key, value in <sequence> if <condition> }`
  - Set comprehension:
  - Generator comprehension:
- Object-oriented programming
  - inheritence
  - polymorphism
  - encapsulation
    - protected member can be accessed by the class and its subclasses.
    - private member can only be accessed from within the class.
  - abstraction
```python
# encapsulation
class Alpha:
  def __init__(self):
      self._a = 2.  # Protected member ‘a’
      self.__b = 2.  # Private member ‘b’

# inheritence
class Parent:
    Members of the parent class

class Child(Parent):
    Inherited members from parent class
    Additional members of the child class
```

- inheritence
```python
# multiple inheritence

# multi-level inheritence
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a) # c.a = 2

# super() : it helps you add the initialization of base class with the derived class.
class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()
```
 
- abstract classes and methods



## Modules, packages, libraries and tools
- Advantages of using modules in python
  - Reusability:
  - Simplicity: Each module is designed for a specific purpose, which helps maintain simplicity and reduces interdependencies.
- import
- namespacing and scope
  - scope: local, enclosed, global, built-in
- reload()
- packages: numpy, pandas, matplotlib ...
- ML packages
- web framework: Django, flask...
- test
  - test type: 
    - unit testing, integration testing, system testing, and acceptance testing.
    - Testing can also be categorized as white box (knowledge of code) and black box (no knowledge of internal workings).
  - pytest
    - `python3 -m pytest test_file.py`
    - `py.test test_file.py`
- test driven development
  - Step 1: Write a test for a feature that fails.
  - Step 2: Write the code to make the test pass.
  - Step 3: Run the test, expecting it to fail initially.
  - Step 4: Evaluate errors and refactor the code as needed.
  - Step 5: Rerun the tests until all pass (green).

