def pyDivisors(n):
    ''' return a list of all divisors of n'''
    divisorList = []
    for i in range(1,n+1):
        #print('n=',n,'i=',i,' n%i=',n%i) #debug
        if n%i==0:
            divisorList.append(i)
    return divisorList
