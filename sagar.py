def field3(tot):
    f3=[]
    for i in range(tot+1,tot+10):
        c=0
        for j in range(2,i):
            if(i%j==0):
                c=c+1
        if(c==0):
            prime=i
            break
    f3.append(prime-tot)
    print(f3[0])
    
n=2 
tot=[] 
for k in range(n):
    f1=int(input())
    f2=int(input())
    tot.append(f1+f2)
field3(tot[0])
field3(tot[1])