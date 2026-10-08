n=[1,2,3,4,5]
k=2
res=[]
for i in range(len(n)-k,len(n)):
  res.append(n[i])
for i in range(0,len(n)-k):
  res.append(n[i])
print(res)  
  
  
  
