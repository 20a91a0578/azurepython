# PERFECT NUMBER
def isperfect(k):
    sum=1
    for i  in range(2,(k//2)+1):
        if k%i==0:
            sum=sum+i
    if sum==k:
        return True
    else:
        return False


n=int(input())
res=isperfect(n)
print(res)



#second and efficient way
import math as m
def isperfect(k):
    s=1
    i=2
    l=int(m.sqrt(k))
    while i!=l:
        if k%i==0:
            s=s+i+(k//i)
        i+=1
    if s==k:
        return True
    else:
        return False


n=int(input())
res=isperfect(n)
print(n,' is perfect number') if res else print(n,' is not perfect number')
