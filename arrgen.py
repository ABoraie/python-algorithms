#Generates a array of length l
import random
def rArray(l):
    A = []
    for x in range(l):
        A.append(random.randint(1,l+1))
    return A
