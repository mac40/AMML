# A=[4,2,5,3,1]
# print(A)
# for i in range(0,4):
#     j=i+1
#     while j<5:
#         print(i,j)
#         if A[i]>A[j]:
#             A[i],A[j]=A[j],A[i]
#             print(A)
#         j=j+1

## Bubble pseudo-python
def bubblesort(iterable):
     seq = list(iterable)
     for passesLeft in range(len(seq) - 1, 0, -1):
         for index in range(passesLeft):
             print(passesLeft,index)
             if seq[index] > seq[index + 1]:
                 seq[index], seq[index + 1] = seq[index + 1], seq[index]
     return seq

A=[5,4,3,2,1]
print(bubblesort(A))