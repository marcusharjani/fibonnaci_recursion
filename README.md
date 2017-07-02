# Fibonnaci Number Recursion HackerRank Challenge!

Following is my solution to the [Fibonnaci Recursion Challenge](https://www.hackerrank.com/challenges/ctci-fibonacci-numbers).

## The Challenge

We are given the following information:

```
The Fibonacci Sequence 
The Fibonacci sequence begins with fibonacci(0) and fibonacci(1) as its respective first and second terms. After these first two elements, each subsequent element is equal to the sum of the previous two elements.

Given n, complete the fibonacci function so it returns fibonacci(n).
```

## The Solution

This is actually a fairly straightforward task. We have to build an algorithm that, after the first two elements (which are 0 and 1), returns for n an integer equal to the sum of the previous two elements.

```
def fibonacci(n):
    twobehind = 0
    behind = 1
```

We start by creating a method that takes in some integer n, `fibonacci(n)`. We define two variables as 0 and 1 we will use these numbers to begin the fibonnaci calculation, since this requires adding the previous two elements, we will name (creatively) these variables `twobehind` and `behind`. Next, we define another variable `i` for iteration and behind our algorithm:

```
    i = 0
    while i < (n - 1):
        current = twobehind + behind
        twobehind = behind
        behind = current
        i = i + 1
```

We will loop through our alogorithm so long as i is less than our `n`. Simply, our current fibonnaci sequence is equal to the sum of the two prior elements. Then we set our two prior elements to one element over as we iterate. 

```
    if (n == 0) or (n == 1):
        return n
```

We are also given a conditional statement that will simply return n if n is equal to the first two numbers in the fibonacci sequence. So finally we say

```
    return current
```


