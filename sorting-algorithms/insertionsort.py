A = [3,5,1,8,2]
i = 1
while i < len(A):
    j = i
    while j > 0 and A[j-1] > A[j]:
        A[j], A[j-1] = A[j-1], A[j]
        j=j-1
    i = i+1
print ''.join(str(e) for e in A)    
