def data_type(data):
  
  if data == None:
    return 'no value'
  
  elif type(data) == str:
    return len(data)
    
  
  elif type(data) == bool:
    return data
    
  elif type(data) == int:
    if data < 100:
      return 'less than 100'
    elif data > 100:
      return 'more than 100'
    return 'Equal to 100'
    
  elif type(data) == list:
    if len(data) - 1 >= 2:
      return data[2]
    return None