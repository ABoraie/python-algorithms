import sys
sys.path.insert(0,'..')
import arrgen
A = arrgen.rArray(100)
print ' '.join(str(e) for e in A) 
print "\n"
#Mergesort#
def merge(A1,A2):
    C = []
    while(len(A1) != 0 and len(A2) != 0):
        if( A1[0] > A2[0] ):
            C.append(A2[0])
            A2.pop(0)
        else:
            C.append(A1[0])
            A1.pop(0)
    while(len(A1) > 0):
        C.append(A1[0])
        A1.pop(0)
    while(len(A2)> 0):
        C.append(A2[0])
        A2.pop(0)
    return C


def mergesort(A):
    if(len(A)<=1):
        return A
    else:
        A1 = mergesort(A[0:len(A)/2])
        A2 = mergesort(A[len(A)/2:len(A)])

        return merge(A1,A2)
        
A = mergesort(A)
print ' '.join(str(e) for e in A)
