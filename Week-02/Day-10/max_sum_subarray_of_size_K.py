arr = [2, 1, 5, 1, 3, 2]
k = 3
sum=0
maxi=0
for i in range(k):
  sum=sum+arr[i]
maxi=max(maxi,sum)  
for i in range(k,len(arr)):
  sum=sum+arr[i]-arr[i-k]
  maxi=max(maxi,sum)
print(maxi)  
  
  
  
  
