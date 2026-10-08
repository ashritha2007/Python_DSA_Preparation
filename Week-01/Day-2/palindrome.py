n=list(map(int,input().split()))
l=0
r=len(n)-1
ispalindrome=True
while(l<r):
  if n[l]!=n[r]:
    ispalindrome=False
    break
  else:
    l=l+1
    r=r-1
if ispalindrome:
  print("Palindrome")
else:
  print("Not a Palindrome")
    

  
  
  
