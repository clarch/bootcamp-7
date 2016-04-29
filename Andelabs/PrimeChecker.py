class PrimeChecker():
  
  def __init__(self, number):
    self.number = number
    
  def is_prime(self):
    if None:
      return False
    else:
      for i in range(2, self.number+1):
        if self.number % i == 0:
          return False
      return True

obj = PrimeChecker('67')
print obj.is_prime()
