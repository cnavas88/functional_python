# functional_python

Repository to write example and solutions in python for functional programming

## Pure functions

These functions have two main properties. First it always produces the same output for the same arguments. It does not change or modifies the input variable.

The functions written like pure functions are easier of test.

## Variables are Inmutability

In python we have inmutability and mutability types.
The numbers, strings and tuples are inmutability, and the list are mutability.

The lists are mutable:

```python
>>> lista = [1, 2, 3, 4]
>>> lista[0] = 5
>>> lista
[5, 2, 3, 4]
```

The tuples are not inmutables:

```python
>>> tuple = (1, 2, 3, 4)
>>> tuple[0] = 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

The strings are also sequences, like lists and tuples, and as such we can access their individual characters:

```python
>>> sentence = "the mobile is broken."
>>> sentence[2]
e
```

But we can't modify it:

```python
>>> sentence[2] = "k"
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    serie[3] = 'k'
TypeError: 'str' object does not support item assignment
```

So, the strings are inmutables too.

Numbers are inmutable:

```python
>>> x = 5
>>> y = x
>>> y
5
>>> x = 6
>>> y
5
```

But let's see the last example with lists:

```python
>>> x = [1, 2, 3, 4]
>>> y = x
>>> y
[1, 2, 3, 4]
>>> x[0] = 5
>>> x
[5, 2, 3, 4]
>>> y
[5, 2, 3, 4]
```

this goes through the concept of reference. In python all are objects, and these objects are stored in memory and have a unique id (memory address). We can know this id with the function id(). When you create a X variable you are actually creating a reference (similar to pointers in C or golang).

``` python
>>> x = 5
>>> id(x)
137396064
>>> y = x
>>> id(y)
137396064
```

It's the same reference because the two variables point to the same object. This is a radically different concept from that of the variables in other languages, in which the content of x and y would be in different directions of memory.

``` python
>>> x = 6
>>> id(x)
137396080
>>> id(y)
137396064
```

A new object has been created, with a value of 6, and now x points to that value. This is also very different from what would happen in other languages: the variable x would continue in the same memory direction, having only modified its content.

But, let's see the same example with lists:

```python
>>> x = [1, 2, 3, 4]
>>> y = x
>>> id(x)
170964396
>>> id(y)
170964396
```

by the moment, everything is exactly the same as before: a single object has been created, the list [1, 2, 3, 4], which is referenced by two variables, x and y. Let's modify:

```python
>>> x[0] = 5
>>> id(x)
170964396
>>> id(y)
170964396
```

In the previous example, when we did x = 6, a new object was created. In the case of the list, we have modified the object itself in situ, taking advantage of its mutability. 

Other situation:

``` python
>>> x = [1, 2, 3, 4]
>>> y = x
>>> x = [5, 2, 3, 4]
>>> y
[1, 2, 3, 4]
>>> id(x)
170489580
>>> id(y)
170791756
```

Notice the important difference: by doing x = [5, 2, 3, 4] we have created a different object, so that x and y point to different objects and so their values now differ. In the previous case, by doing x [0] = 5 we directly modified the same object and no new one was created.

## Functions are First-Class and can be Higher-Order

First-class objects are handled uniformly throughout. They may be stored in data structures, passed as arguments, or used in control structures. A programming language is said to support first-class functions if it treats functions as first-class objects. 

Properties of first class functions:

- A function is an instance of the Object type.
- You can store the function in a variable.
- You can pass the function as a parameter to another function.
- You can return the function from a function.
- You can store them in data structures as hash tables, lists, ...
- Nested functions called Closures.

Python has 3 first-class functions:

### Map

map is a function that takes a set of inputs and transform them into another set based on a process (function) specified. 

The map function is useful when we want to do something to all values in a collection.

### Filter

filter, as the name suggests, is a function that helps “filter” out unwanted items. For example, we may want to filter out all the odd numbers from scores.

### Reduce

It is used to make calculations from an iteration. Its structure has 3 arguments: the expression, the element we want to go through and the starting variable. You can find it inside the functools library.

## Recursion

In functional programming, there is not concept of 'for' or 'while' loop, instead recursion is used. Recursion is a process in which a functions calls itself directly or indirectly.

## Lambda functions

In python, anonymous function means that a functions without name. As we already know that def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.

- This function can have any number of arguments but only one expression, which is evaluated and returned.
- One is free to use lambda functions wherever function objects are required.
- You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.

## Decorators

Python has an interesting feature called decorators to add functionality to an existing code.

This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time.

## Lists comprehensions

List comprehensions provide a concise way to create lists.

It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.

- List comprehension is an elegant way to define and create lists based on existing lists.
- List comprehension is generally more compact and faster than normal functions and loops for creating list.
- Remember, every list comprehension can be rewritten in for loop, but every for loop can't be rewritten in the form of list comprehension.