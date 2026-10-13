height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
l=0
maximum=0
r=len(height)-1
while(l<r):
  area=min(height[l],height[r])*(r-l)
  maximum=max(maximum,area)
  if height[l]<height[r]:
    l=l+1
  else:
    r=r-1
print(maximum)  
  
