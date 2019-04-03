# Python Recursion

## Problem

> Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial). Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0. - [HackerRank](www.hackerrank.com)

## Process

```python
# NOTE Use recursion
# Given n, return n * (n-1) * ((n-1)-1)
# (n-1) needs to be repeated, so that will be the recursion part
# Needs a stop when n is 1, therefore return 1 if n is 1
```

### Given n, return n * (n-1)

```python
def factorial(n):
  return n * (n-1)
```

### (n-1) needs to be repeated, so that will be the recursion part

```python
def factorial(n):
  return n * factorial(n-1)
```

### Needs a stop when n is 1, therefore return 1 if n is 1

```python
def factorial(n):
  return 1 if n == 1 else n * factorial(n-1)
```

## Conclusion
The hardest part is understanding when and how to use recursion. It is always best to write out a simple example and when it repeats could be a sign.
