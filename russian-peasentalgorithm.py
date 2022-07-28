def multip(a,b):
    c=0
    while a>0:
        
        if a%2!=0:
            c+=b
        a=int(a/2)
        b=b*2
        print(a,'  ',b)
    return c




a,b=map(int,input().split())
res=multip(a,b)
print(res)


