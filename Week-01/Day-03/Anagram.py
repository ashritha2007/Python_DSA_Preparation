s="listen"
s1="silent"
d={}
for i in s:
  if i in d:
    d[i]=d[i]+1
  else:
    d[i]=1
for i in s1:
  if i in d:
    d[i]=d[i]-1
  else:
    d[i]=1
isanagram=True    
for i in d:
  if d[i]!=0:
    isanagram=False
if isanagram:
  print("A")
else:
  print("NA")
    
    
    
  
  
