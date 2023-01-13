import random

#mutating the offsprings
#reversing i-j positions
#here reverse 2-7
#mutating all offsprings
def mutate(offsprings):
    n=len(offsprings)
    perc=.7
    idx=random.sample(range(0,n),int(perc*n))

    for i in idx:
        l=offsprings[i]
        n=len(l)
        m=int(n/2)
        start=m-int(n/3)
        end=m+int(n/3)
        l[start:end]=l[start:end][::-1]
        offsprings[i]=l
    return offsprings
