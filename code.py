#########################
# !!! SOLUTION CODE !!! #
#########################

def factorial(n):
  """Calculates the factorial"""
  return n * factorial(n-1) if n != 1 else 1
