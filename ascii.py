m={}
while 1:
 try:s=raw_input('');l=s.split(' ');t=l[0]+','+l[1];m[t]=int(l[2])
 except:break
for y in range(40):
 o=''
 for x in range(80):
  c=str(x)+','+`y`
  if c in m:o+=chr(m[c])
  else:o+=' '
 A=o.rstrip()
 if A!='':print A
