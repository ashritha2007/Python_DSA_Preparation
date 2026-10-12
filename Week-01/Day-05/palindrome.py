s ="A man, a plan, a canal: Panama"
s=s.lower()
res=""
for i in s:
  if i.isalnum ():
    res=res+i
if res==res[::-1]:
  print("palindrome")
else:
  print("Not")
