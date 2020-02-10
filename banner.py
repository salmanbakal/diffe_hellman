def banner(message: str):
  """
  Convert a message string into a banner. 
  Example:
    message = "It's a wonderful worlds!"
    becomes
    *************
    * It's      *
    * a         *
    * wonderful * 
    * world!    *
    *************
                                                      
  """

  out=[]
  names=message.split()
  longest = max(names, key=len)
  len_max = len(longest)
  star_line='*'*(len_max+4)
  out.append(star_line)
  for i in names:
    space_len=len_max-len(i)
    trailing_spaces = ' ' * space_len
    out.append(f"* {i}{trailing_spaces} *")
  out.append(star_line)
  return "\n".join(out)

def bannerIO():
  print("")
  print("Function Banner")
  print("")
  print("Enter a message: ")
  message = input()  
  print("Result:")
  print(banner(message))
bannerIO()
