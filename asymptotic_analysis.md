# Asymptotic analysis

## Big Theta Θ

T(n)= Θ(n<sup>2</sup>)

Θ(g(n)):={ f(n):exists positive const c<sub>1</sub>,c<sub>2</sub>>0, and n<sub>0</sub> such that 0<=c<sub>1</sub>g(n)<=f(n)<=c<sub>2</sub>g(n) for all n>=n<sub>0</sub>}

![big theta](immagini/Screenshot_1.png)

## Big Oh O

O(g(n)) = { f(n) : there exist positive constants c and n<sub>0</sub> such that 0<=f(n)<=cg(n) for all n>=n<sub>0</sub>}

Θ(g(n)) is subset of O(g(n))

![big oh](immagini/Screenshot_2.png)

## Prefix Averages calculation

X[1÷n] calculate A[i] = (Σ<sub>j=1->i</sub>X[j])/i

### Prefix averages(X)
```javascript
n=X.length
A=[]
A.len()=n
for i=1 to n
    a=0
    for j=1 to i
        a=a+X[i]
    A[i]=a/i
return A
```

line|cost
---|---
2|O(n)
4|O(n)
6|O(n<sup>2</sup>)

T(n)=O(n)+O(n)+__O(n<sup>2</sup>)__