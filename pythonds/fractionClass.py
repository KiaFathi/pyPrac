#Fractions
  #methods I want
    #Add
    #Subtract
    #Multiply
    #Divide


#Euclid's algorithm for GCD
  # gcd of m and n = n if m%n == 0
  # else 
    # gcd of m and n = gcd of n and m%n
  # only works if denominator is positive

def gcd(m, n):
  while m % n != 0:
    newN = m % n
    m = n
    n = newN
  return n


class Fraction:
  
  def __init__(self, numerator, denominator):
    self.num = numerator
    self.den = denominator

  def __str__(self):
    return str(self.num) + '/' + str(self.den)

  def __add__(self, otherFraction):
    newNum = self.num * otherFraction.den + otherFraction.num * self.den
    newDen = self.den * otherFraction.den
    commonDenominator = gcd(newNum, newDen)
    return Fraction(newNum/commonDenominator, newDen/commonDenominator)

  def __eq__(self, otherFraction):
    return self.num * otherFraction.den == self.den * otherFraction.num

  def __lt__(self, other):
    return self.num * other.den < self.den * other.num
  
  def __gt__(self, other):
    return self.num * other.den > self.den * other.num
    
  def __sub__(self, otherFraction):
    newNum = self.num * otherFraction.den - otherFraction.num * self.den
    newDen = self.den * otherFraction.den
    commonDenominator = gcd(newNum, newDen)
    return Fraction(newNum/commonDenominator, newDen/commonDenominator)

  def __mul__(self, otherFraction):
    newNum = self.num * otherFraction.num
    newDen = self.den * otherFraction.den
    commonDenominator = gcd(newNum, newDen)
    return Fraction(newNum/commonDenominator, newDen/commonDenominator)

  def __div__(self, otherFraction):
    newNum = self.num * otherFraction.den
    newDen = self.den * otherFraction.num
    commonDenominator = gcd(newNum, newDen)
    return Fraction(newNum/commonDenominator, newDen/commonDenominator)



myFraction = Fraction(6,10)
yourFraction = Fraction(1,10)
print(myFraction)

print(myFraction + yourFraction)
print(myFraction == Fraction(9, 15))

print('%s minus %s = %s' %(myFraction, yourFraction, myFraction-yourFraction))
print('%s times %s = %s' %(myFraction, yourFraction, myFraction*yourFraction))
print('%s divided by %s = %s' %(myFraction, yourFraction, myFraction/yourFraction))
print('%s is greater than %s' %(myFraction, yourFraction), myFraction > yourFraction)
print('%s is less than %s' %(myFraction, yourFraction), myFraction < yourFraction)
