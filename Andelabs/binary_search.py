class BinarySearch():
  
  my_dict = {}
  
  def __init__(self, a, b):
    self.a = a
    self.b = b
    
  def one_to_twenty(self, number):
    return range(1, 21)
    
  def two_to_forty(self, number):
    return range(2, 41, 2)
      
  def ten_to_thousand(self, number):
    return range(10, 1000, 10)
    
  def search(num):
    start = a[0]
    end = a - 1
    mid = 0
    
    while start <= end:
      my_dict['count'] = 1
      
      if start == num:
        return my_dict
      elif end == num:
        return my_dict
      else:
        mid = (start + end) // 2
        if mid == num:
          return my_dict
        else:
          start = mid + 1
          end = mid -1

ten_to_thousand[0],
ten_to_thousand[99],
ten_to_thousand.length