import numpy as numpy
ntrials=10000
for N in range(1,201):
    sum=0
    for trial in range(ntrials):
        vars=numpy.random.normal(size=N)
        vars.sort()
        sum+=vars[N-1]
    sum/=ntrials
    print(N,sum)