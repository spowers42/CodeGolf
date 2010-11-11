r=raw_input('');e={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000};s=0;l=0;c=0
for c in r:
    c=e[c]
    if c>l&l!=0:s-=l
    else:s+=l
    l=c
s+=l;print s

