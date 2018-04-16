A=[5,4,3,2,1]
n=len(A)
j=0
while j<n-1:
    smallest=j
    i=j+1
    while i<n:
        if A[i]<A[smallest]:
            smallest=i
        i=i+1
    A[j],A[smallest] = A[smallest],A[j]
    j=j+1
print(A)