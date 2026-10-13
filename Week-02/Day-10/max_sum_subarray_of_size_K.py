arr = [2, 1, 5, 1, 3, 2]
k = 3
sum1=0
maxi=0
for i in range(k):
  sum1=sum1+arr[i]
maxi=max(maxi,sum1)  
for i in range(k,len(arr)):
  sum1=sum1+arr[i]-arr[i-k]
  maxi=max(maxi,sum1)
print(maxi)  
  
  
  
  
