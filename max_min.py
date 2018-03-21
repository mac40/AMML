A=[12,1,5,67,5,66,33,5,6,3]

max=A[0]
min=A[0]

for el in A[1:]:
    if el>max:
        max=el
    if el<min:
        min=el
print(min,max)