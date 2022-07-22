#perfect number
import math as m
def isperfect(k):
    s=1
    i=2
    l=int(m.sqrt(k))
    while i!=l+1:
        if k%i==0:
            s=s+i+(k//i)
        i+=1
    print(s)
    if s==k:
        return True
    else:
        return False

t=int(input())
for _ in range(t):
    n=int(input())
    res=isperfect(n)
    print(n,' is perfect number') if res else print(n,' is not perfect number')



#spy number
def isspy(n):
    s=0
    p=1
    while n:
        r=n%10
        s+=r
        p*=r
        n=n//10
    if s==p:
        return True
    else:
        return False



t=int(input())
for _ in range(t):
    n=int(input())
    res=isspy(n)
    print(res)



#automorphic number
import math as m
def isautomorph(n):
    k=str(n)
    l=len(k)
    p=n**2
    o=int(p%(m.pow(10,l)))
    if n==o:
        return True
    else:
        return False


t=int(input())
for _ in range(t):
    n=int(input())
    res=isautomorph(n)
    print(res)



#semiprime number
def isprim(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def issemiprim(n):
    for i in range(2,n//2+1):
        if n%i==0:
            if isprim(i) and isprim(n//i):
                return True
    return False




n=int(input())
res=issemiprim(n)
print(res)


#self dividing numbers

def isselfdivid(n):
    t=n
    while t>0:
        r=t%10
        if n%r!=0:
            return False
        t=t//10
    return True


t=int(input())
for _ in range(t):
    n=int(input())
    res=isselfdivid(n)
    print(res)
