def search(array,element1,element2):
 count=0
 for e in array:
  if e == element2:
   count=count+1
 if count == element1:
  return True
 return False
"This method returns true if there are element1 of element2 in array. Else returns false" 
