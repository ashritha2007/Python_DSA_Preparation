arr = [2, 0, 2, 1, 1, 0]
l=0
i=0
r=len(arr)-1
while(i<=r):
  if arr[i]==2:
    arr[i],arr[r]=arr[r],arr[i]
    r=r-1
  elif arr[i]==0:
    arr[i],arr[l]=arr[l],arr[i]
    l=l+1
    i=i+1
  else:
    i=i+1
print(arr)    
