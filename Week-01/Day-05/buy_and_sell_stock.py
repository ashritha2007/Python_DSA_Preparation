p=[7,1,5,3,6,4]
maxi=0
for i in range(len(p)):
  for j in range(i+1,len(p)):
    s=p[j]-p[i]
    maxi=max(maxi,s)
print(maxi)    
    
