A=[5,4,3,2,1] # Array to be ordered
n=len(A) # length of Array
ordered=False # flag in charge of breaking the loop, when no swaps are preformed the array is ordered and the algorithm can stop
# PRE:
#   A is an array of numbers
#   n is the lengh of the array
#   ordered is a boolean var initialized to False
while not ordered: # the algorithm goes on until no permutations are performed
# INV:
#   A is one possible permutation of the original A array
#   n is the length of the array non ordered by the algorithm
#   ordered is False if a permutation has been executed, True otherwise
    ordered=True # ordered is set to True. It will be changed to false if a permutation is performed in this cycle
    i=0 # iterator
    while i<n-1: # make the n pair-wise comparisons of the cycle
        if A[i]>A[i+1]: # make the pair-wise comparison between elements i and i+1, if A[i]>A[i+1] then swap the elements
            dummy=A[i]      #
            A[i]=A[i+1]     # swap elements
            A[i+1]=dummy    #
            ordered=False # turn ordered to False since a permutation has been executed
        i=i+1 # iterator increase
# POST:
#   A is the increasingly ordered permutation of original A
print(A)