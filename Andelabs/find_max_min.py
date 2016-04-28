def find_max_min(Arr):
  
  max_, min_ = Arr[0], Arr[0]
  min_max = []
  
  for arr in Arr:
    if arr < min_:
      min_ = arr
    if arr > max_:
      max_ = arr

  if min_ == max_:
    length = len(Arr)
    return min_max.append(length)
  else:
    min_max.append()

print find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2])
print find_max_min([4, 4, 4, 4])