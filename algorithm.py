def search(array,element1,element2):

 count=0
 for e in array:
  if e == element2:
   count=count+1

 if count == int(element1):
  return True
 return False

