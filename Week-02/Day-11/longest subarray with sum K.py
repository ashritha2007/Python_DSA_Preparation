s = "abcabcbb"
S=set()
maxi=0
l=0
for i in range(len(s)):
  while s[i] in S:
    S.remove(s[l])
    l=l+1
  else:
    S.add(s[i])
    maxi=max(maxi,i-l+1)
print(maxi)    
    
