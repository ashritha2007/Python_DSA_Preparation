s = "abc"
t = "abd"
d={}
isanagram=True
for i in s:
  if i in d:
    d[i]=d[i]+1
  else:
    d[i]=1
for i in t:
  if i in d:
    d[i]=d[i]-1
  else:
    d[i]=-1
for i in d:
  if d[i]!=0:
    isanagram=False
    break
if isanagram:
  print("anagram")
else:
  print("not")
    
  
