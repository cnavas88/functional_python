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

## Functions are First-Class

## Recursion