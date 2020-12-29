alphabet='AABCCDEEFJJK'
substring=''
factor=3
count=0
for k in alphabet:
  if k not in substring:
    substring+=k
  count+=1
  if count == factor:
    print(substring)
    count=0
    substring=''