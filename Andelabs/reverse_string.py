def reverse_string(string):
    length = len(string)
    new_str = ""
    
    if string:
      for i in range(length - 1, -1, -1):
          new_str += string[i]
      return new_str
      
    return None