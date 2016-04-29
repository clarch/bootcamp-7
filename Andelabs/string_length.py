def string_length(word):
  length = []
  
  if type(word) == str:
    leng = length.append(len(word))
    return length
    
  elif isinstance(word, list):
    for i in word:
      length.append(len(i))
    return length
  
print string_length(["ann", "mark"])
print string_length("ann")