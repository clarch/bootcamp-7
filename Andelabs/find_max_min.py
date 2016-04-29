def find_max_min(Arr):
  max_, min_ = Arr[0], Arr[0]
  Min_Max = []
  
  for arr in Arr:
    if arr < min_:
      min_ = arr
    elif arr > max_:
      max_ = arr
  
  if min_ == max_:
    Min_Max.append(len(Arr))
    return Min_Max
  else:
    Min_Max.append(min_)
    Min_Max.append(max_)
    return Min_Max