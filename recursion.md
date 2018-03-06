# Recursion

## Divide et Impera

* __Divide__ the problem into smaller sub-problems
* __Conquer__ the sub-problems by solving them one at a time
* __Combine__ the solutions of the subproblems into the solution for the general problem

### Iterative vs Recursive

#### power(x,n)

##### Iterative

```javascript
power(x,n){
    result=1
    for i=1 to n:
        result=result*x
    return result
}
```

##### Recursive

```javascript
power(x,n){
    if(n==1)
        return x // base case
    else
        return x*power(x,n-1) // recursive step
}
```

### Execution stack

When an algorithm calls itself (nested call):
1. the current execution is paused
2. the execution context associated with the current alg exec is stored in a stack
3. the nested call executes
4. after it ends the previous exe context is retrieved from the stack and the execution is resumed from where it stopped

### Merge-Sort

1. Assume to have an unordered sequince of n elements
2. __Divide__ the sequence in two sequences with length n/2
3. __Impera__: sort the two sequences using merge-sort recursively
4. __Combine__: merge the two ordered sequences into the output sequence

![Merge-sort](immagini/Screenshot_3.png)

