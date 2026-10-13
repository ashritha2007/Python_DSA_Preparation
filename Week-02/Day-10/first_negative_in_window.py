arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
arr1=[]
for i in range(len(arr)-k+1):
  for j in range(i,i+k):
    if arr[j]<0:
      arr1.append(arr[j])
      break
  else:
      arr1.append(0)
print(arr1)      
