array_1=[]
def array_of_list(no_of_elements):
    for elems in range(no_of_elements):
      elements = int(input('enter the elements'))
      array_1.append(elements)
    return ''

def count_in_setA(no_of_elements_in_set):
  setA=[]
  happiness=0
  for set0 in range(no_of_elements_in_set):
    sets_elems=int(input('enter the set elements of set A\n'))
    setA.append(sets_elems)
  for element in setA:
    if element in array_1:
        happiness+=1
    else:
      pass
  print(f'your happiness is {happiness}')
  return '' 

def count_in_setB(no_of_elements_in_set):
  setB=[]
  happiness=0
  for set1 in range(no_of_elements_in_set):
    sets_elems=int(input('enter the set elements of set B\n'))
    setB.append(sets_elems)
  for element in setB:
    if element in array_1:
        happiness-=1
    else:
      pass 
  print(f'your happiness is {happiness}')
  return ''      
           

def main():
    
    no_of_elements = int(input('enter the no of elements in array\n'))
    no_of_elements_in_set = int(input('enter the no of elements in each sets\n'))
    print(array_of_list(no_of_elements))
    print(count_in_setA(no_of_elements_in_set))
    print(count_in_setB(no_of_elements_in_set))
main()

