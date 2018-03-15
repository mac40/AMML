def binsearch(A, t, l, r, m):
    if(l > r):
        return(m)
    else:
        if(A[m] <= t):
            l = m + 1
            m = (r + l) // 2
            return binsearch(A, t, l, r, m)
        if(A[m] > t):
            r = m - 1
            m = (r + l) // 2
            return binsearch(A, t, l, r, m)


A = [1, 2, 3, 4, 5]
l = 0
r = len(A) - 1
t = int(input("Array=[1,2,3,4,5] what element do you want to find?"))
m = (r + l) // 2

while l < r:
    if(A[m] <= t):
        l = m + 1
        m = (r + l) // 2
    if(A[m] > t):
        r = m - 1
        m = (r + l) // 2
print("Iterative result = {}".format(m))

sol = binsearch(A, t, l, r, m)

print("Recursive result = {}".format(sol))
