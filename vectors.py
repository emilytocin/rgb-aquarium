# A simple integer 2Dvector lib.

import random
import math

def DistanceSqr(v1, v2):
  return math.pow(v1.x - v2.x, 2) + math.pow(v1.y - v2.y, 2)
  
def Distance(v1, v2):
  math.sqrt(DistanceSqr(v1, v2))

class Vec(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Vec(self.x + other.x, self.y + other.y)
    
  def __sub__(self, other):
    return Vec(self.x - other.x, self.y - other.y)
    
  def __mul__(self, scalar):
    # other is expected to be an int.
    return Vec(int(self.x * scalar), int(self.y  * scalar))
  
  def __div__(self, divisor):
    return self * (1 / divisor)
  
  def magSqr(self):
    return DistanceSqr(self, Vec(0, 0))
  
  def mag(self):
    return Distance(self, Vec(0, 0))


def RandomDirectionNormal():
  # This is really just asking for ((-1|0|1), (-1|0|1)).
  # But it has to not have two zeros.

  x = random.randint(-1, 1)
  y = random.randint(-1, 1)

  # Lord Forgive Me
  if (x == 0 and y == 0):
    if random.randint(1, 2) == 1:
      if random.randint(1, 2) == 1:
        x = -1
      else:
        y = -1
    if random.randint(1, 2) == 1:
      if random.randint(1, 2) == 1:
        x = 1
      else:
        y = 1

  return Vec(x,y)
