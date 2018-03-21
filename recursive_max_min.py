def maxmin(A,b,e):
    solution = [0,0]
    midsol = [0,0,0,0]
    if b==e:
        solution[0],solution[1]=A[b],A[e]
    else:
        mid=(b+e)//2
        midsol[0],midsol[1] = maxmin(A,b,mid)
        midsol[2],midsol[3] = maxmin(A,mid+1,e)
        if midsol[1]<midsol[3]:
            solution[1] = midsol[3]
        else:
            solution[1] = midsol[1]
        if midsol[0]>midsol[2]:
            solution[0] = midsol[2]
        else:
            solution[0] = midsol[0]
    return solution[0],solution[1]

A = [34,1,342,42,44,2,123,5]

min,max=maxmin(A,0,len(A)-1)

print(min,max)