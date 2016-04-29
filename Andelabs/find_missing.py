def find_missing(arr1, arr2):
  
  miss_num = []
  
  if len(arr1) == 0 and len(arr2) == 0:
    return 0
    
  elif arr1 == arr2:
    return 0
    
  else:
    len1 = len(set(arr1))
    len2 = len(set(arr2))
    
    if len1 > len2:
    	return list(set(arr1) - set(arr2))
      
    elif len1 > len2:
    	return list(set(arr1) - set(arr2))

print find_missing([2, 3, 4, 5, 6], [4, 5, 6])
list1 = find_missing([2], [2])
list2 = find_missing([4], [4])
list3 = find_missing([7], [7])
print find_missing([2], [2])
print find_missing([4], [4])
print find_missing([7], [7])