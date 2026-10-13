arr = [1, 1, 2, 2, 3, 4, 4]
i=1
pos=0
for i in range(len(arr)):
  if arr[i]!=arr[pos]:
    pos=pos+1
    arr[pos]=arr[i]
print(arr[:pos+1])
  
