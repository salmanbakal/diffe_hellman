string = 'qwertyuiopasdfghjk'
width = 4
i,j=0,width
while j <= len(string):
  parts=string[i:j]
  print(parts)
  i,j=j,j+4