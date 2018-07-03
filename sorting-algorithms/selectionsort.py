import sys
sys.path.insert(0,'..')
import arrgen
A = arrgen.rArray(100)
print ' '.join(str(e) for e in A) 
print "\n"
def selectionsort(A):
    for x in range(0,len(A)):
        minimum = x

        for y in range(x,len(A)):
            if(A[y]<A[minimum]):
                minimum = y
        A[x],A[minimum] = A[minimum],A[x]
    return A

A = selectionsort(A)
print ' '.join(str(e) for e in A)    

