# Design and Analysis of Algorithms
* __Definition__: An algorithm is a well-defined _computational procedure_ that takes some values as __input__ and produces some values as __output__
* An Algorithm is a sequence of instructions to describe the solution of a problem
* Algorithms are useful to describe what we are doing
## Euclid's algorithm
* Given two positive numbers n and m find their greates common divisor
    1. Divide m by n  and let r be the remainder
    2. if r=0, the algorithm ends; n is the answer
    3. set m=n, n=r, and go back to first step
## Knuth's five rules
1. __Finiteness__: It must always terminate after a _finite_ number of steps.
2. __Definiteness__: Each step must be precisely defined
3. __Input__: It has zero or more inputs.
4. __Output__: It has one or more outputs.
5. __Effectiveness__: Its operations must all be sufficiently basic that they can in principle be done exactly in a finite amount of time by someone using pencil and paper.
* An algorithm without finiteness is a _computational method_.
## Algorithms
* Sorting Algorithm
    * __Input__: sequence of _n_ numbers
    * __Output__: a permutation of the input such that the elements are ordered in an increasing order
* An algorithm is the sequence of operations to obtain the sorted list of numbers starting from the unordered one
* We can define the algorithm by using pseudo-code or any available programming language
* one possible __input__ of the algorithm is called an __istance__
* An algorithm is good if it works for _every_ instance
* An algorithm is correct if it halts with the correct output, so we say that an algorithm is correct if it _solves_ the given computational problem
## Computational Problem
* A computational problem _Pi_ is a mathematical relation between a set _I_ of possible instances and a set _S_ of possible solutions: such that for all _i_ in _I_ there exists at least one solution _s_ in _S_ such that (_i,s_) in _Pi_
## Other focuses other than performance
* Correctness
* Cost
* Maintainability (_documentation_)
* Stability and Robustness (_works equally with every instance_)
* Having a wide range of features
* Modularity (_split functionalities as much as possible_)
* Security (_not the focus of the course_)
* User-friendliness (_easy to use_)
## Algorithmic analysis
* It is used to determine how good an algorithm is.
* The idea is to take an algorithm and to determine its _quantitative_ behaviour
    * How many operations...
    * Given two algorithms A and B both solving problem p, do we prefer A or B?
* The core is to determine the performance
## Efficiency
* We should care about efficiency even though computers are getting faster
* Algorithmic efficiency is measured based on the input
* e.g. _Insertion Sort_ requires __c<sub>1</sub>n<sup>2</sup>__ time to sort a sequence of _n_ numbers
# Insertion Sort
* e.g. Ordering cards
## Blackboard example
* Input: A<5,2,4,6,1,3>
* Algorithm starts from the second element
    * the first one is considered already ordered (_it's a single element_)
    * We compare the second element with the first element
        * if second < first swap
* move to the third element
    * compare with prev numbers as long as third < prev
* go on till end

step|1|2|3|4|5|6
---|---|---|---|---|---|---
0|5|__2__|4|6|1|3
1|2|5|__4__|6|1|3
2|2|4|5|__6__|1|3
3|2|4|5|6|__1__|3
4|1|2|4|5|6|__3__
5|__1__|__2__|__3__|__4__|__5__|__6__
## Pseudo-code
Insertion-sort(A)
```javascript
for j=2 to length(A)
    do key=A[j]
    //insert A[j] into the sorted sequence A[1...j-1]
    i=j-1
    while i>0 and A[i]>key
        do A[i+1]=A[i]
        i=i-1
    A[i+1]=key
```
* __Best__ case scenario: __ordered array__
* __Worst__ case scenario: __inverted order array__
# Loop Invariant
* __Initialization__: it is true (_that the algorithm is correct_) before the first iteration of the loop
    * e.g. in insertion-sort all elements before _j_ is already ordered (_e.g. j=2 A[1...j-1]=A[1]=> ordered_)
* __Maintenance__: if it is true _before_ an iteration, it remains true _before_ the start of the next iteration
* __Termination__: When the algorithm terminates invariant gives us the property that the algorithm __is correct__
### Operation cost
The following costs are the individual cost of every line of code previously written
row|cost|times
---|---|---
1 |c<sub>1</sub>| _n_
2 |c<sub>2</sub>| _n-1_
3 |c<sub>3</sub> (_but the cost is 0_)| _n-1_
4 |c<sub>4</sub>| _n-1_
5 |c<sub>5</sub>| _Σ<sub>j=2->n</sub> t<sub>j</sub>_
6 |c<sub>6</sub>| _Σ<sub>j=2->n</sub> t<sub>j</sub>-1_
7 |c<sub>7</sub>| _Σ<sub>j=2->n</sub> t<sub>j</sub>-1_
8 |c<sub>8</sub>| _n-1_
