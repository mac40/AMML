Array = [5,4,3,2,1]
j=1
while j<len(Array):
    key=Array[j]
    i=j-1
    while i>=0 and Array[i]>key:
        Array[i+1]=Array[i]
        i=i-1
    Array[i+1]=key
    j=j+1
print(Array)