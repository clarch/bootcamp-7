def factorial(number):
  result = 1
  
  for num in range(2, number+1):
    result *= num
  return result