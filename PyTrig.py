import math

class mat:
  pi = 3.141592653589793
  e = 2.718281828459045
  phi = (1 + (5 ** 0.5)) / 2

  def __init__(self):
    pass

  def root(self, x, y):
    return x ** (1 / y)

  def log(self, base, x):
    if x <= 0 or base <= 0 or base == 1:
      raise ValueError
    return self.ln(x) / self.ln(base)

  def factorial(self, n):
    if n < 0:
      raise ValueError
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

  def gcd(self, a, b):
    while b:
      a, b = b, a % b
    return a

  def lcm(self, a, b):
    if a == 0 or b == 0:
      return 0
    return abs(a * b) // self.gcd(a, b)

  def ceil(self, a):
    if int(a) == a:
      return int(a)
    return int(a) + 1

  def floor(self, a):
    return int(a)

  def exp(self, a, terms):
    result = 1
    term = 1
    for i in range(1, terms):
      term *= a / i
      result += term
    return result

  def dist(self, x, y, x1, y1):
    return ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5

  def to_radians(self, degrees):
      return degrees * (self.pi / 180)

  def normalize_angle(self, x):
     return x % (2 * self.pi)

  def sin(self, x, terms):
    x = self.normalize_angle(x)
    result = 0
    for n in range(terms):
      term = ((-1) ** n) * (x ** (2 * n + 1)) / self.factorial(2 * n + 1)
      result += term
      return result

  def cos(self, x, terms):
      x = self.normalize_angle(x)
      result = 0
      for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n)) / self.factorial(2 * n)
        result += term
      return result

  def tan(self, x, terms):
      cos_value = self.cos(x, terms)
      if cos_value == 0:
        raise ValueError("Tangent undefined for this angle.")
      return self.sin(x, terms) / cos_value

  def sinh(self, x, terms):
      return (self.exp(x, terms) - self.exp(-x, terms)) / 2

  def cosh(self, x, terms):
      return (self.exp(x, terms) + self.exp(-x, terms)) / 2

  def tanh(self, x, terms):
      sinh_value = self.sinh(x, terms)
      cosh_value = self.cosh(x, terms)
      if cosh_value == 0:
        raise ValueError("Tanh undefined for this input.")
      return sinh_value / cosh_value

  def arcsin(self, x, terms=10):
      if x < -1 or x > 1:
        raise ValueError("arcsin(x) is only defined for -1 <= x <= 1")
      result = 0
      for n in range(terms):
        term = (self.factorial(2*n)*x**(2*n+1))/(4**n * self.factorial(n)**2*(2*n+1))
        result += term
      return result

  def arccos(self, x, terms):
      if x < -1 or x > 1:
          raise ValueError("arccos(x) is only defined for -1 <= x <= 1")
      return self.pi / 2 - self.arcsin(x, terms)

  def arctan(self, x, terms):
      result = 0
      for n in range(terms):
          term = ((-1)**n * x**(2*n+1)) / (2*n+1)
          result += term
      return result

  def arsinh(self, x):
      return self.ln(x + self.root(x**2 + 1,2))

  def arcosh(self, x):
      if x < 1:
          raise ValueError("arcosh(x) is only defined for x >= 1")
      return self.ln(x + self.root(x**2 - 1,2))

  def artanh(self, x):
      if x <= -1 or x >= 1:
          raise ValueError("artanh(x) is only defined for -1 < x < 1")
      return 0.5 * self.ln((1 + x) / (1 - x))

  def ln(self, x, terms=50):
      if x <= 0:
          raise ValueError("ln(x) is only defined for x > 0")
      result = 0
      for n in range(1, terms + 1):
          term = ((-1)**(n+1)) * (x - 1)**n / n
          result += term
      return result
pytrig = mat()
