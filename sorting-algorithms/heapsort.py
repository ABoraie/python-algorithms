import sys
sys.path.insert(0,'..')
import arrgen
A = arrgen.rArray(100)
print ' '.join(str(e) for e in A) 
print "\n"

def heapify(A,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if(left < n and A[i] < A[left]):
        largest = left
    if(right < n and A[largest] <A[right]):
        largest  = right
    if(largest != i):
        A[i],A[largest] = A[largest],A[i]
        A=heapify(A,n,largest)
    return A

def heapsort(A):
    n = len(A)
    for x in range(n,-1,-1):
        A=heapify(A,n,x)
    
    print ' '.join(str(e) for e in A)    
    for x in range(n-1,0,-1):
        A[0],A[x] = A[x],A[0]
        A = heapify(A,x,0)
    return A
A = heapsort(A)
print ' '.join(str(e) for e in A)    
    
