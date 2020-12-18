import re

file = open('input/18.txt', 'r') 
data = [i.strip().replace(" ", "") for i in file.readlines()]

class Na:
  def __init__(self, v):
    self.value = v

  def __add__(self, other):
    return Na(self.value + other.value)

  def __sub__(self, other):
    return Na(self.value * other.value)

class Nb:
  def __init__(self, v):
    self.value = v

  def __truediv__(self, other):
    return Nb(self.value + other.value)

  def __sub__(self, other):
    return Nb(self.value * other.value)

def p1(expr):
  return eval(re.sub("(\d+)", "Na(\\1)", expr).replace("*", "-")).value

def p2(expr):
  return eval(re.sub("(\d+)", "Nb(\\1)", expr).replace("*", "-").replace("+", "/")).value

sample_tokens_p1 = [
  ("2 * 3 + (4 * 5)", 26),
  ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
  ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
  ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632),
]
for s,expected in sample_tokens_p1:
  assert(p1(s) == expected)

sample_tokens_p2 = [
  ("2 * 3 + (4 * 5)", 46),
  ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
  ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
  ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340)
]
for s,expected in sample_tokens_p2:
  assert(p2(s) == expected)

print(sum(map(p1, data)))
print(sum(map(p2, data)))