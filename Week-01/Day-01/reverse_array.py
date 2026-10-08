n=list(map(int,input().split()))
l=0
r=len(n)-1
while(l<r):
  n[l],n[r]=n[r],n[l]
  l=l+1
  r=r-1
print(n)  
