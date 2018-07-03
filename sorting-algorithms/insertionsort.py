import sys
sys.path.insert(0,'..')
import arrgen
A = arrgen.rArray(100)
print ' '.join(str(e) for e in A) 
print "\n"
def insertionsort(A):
    i = 1
    while i < len(A):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j], A[j-1] = A[j-1], A[j]
            j=j-1
        i = i+1
    return A

A = insertionsort(A)
print ' '.join(str(e) for e in A)    
