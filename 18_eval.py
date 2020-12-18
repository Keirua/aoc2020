import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/18.txt', 'r') 
data = [i.strip().replace(" ", "") for i in file.readlines()]

class Na:
  def __init__(self, v):
    self.val = v

  def __add__(self, other):
    return Na(self.val + other.val)

  def __sub__(self, other):
    return Na(self.val * other.val)

  def __repr__(self):
    return str(self.val)


def p1(expr):
  expr = re.sub("(\d+)", "Na(\\1)", expr).replace("*", "-")
  return eval(expr)

sample_tokens = [
  ("2 * 3 + (4 * 5)", 26),
  ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
  ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
  ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632),
]
for s,expected in sample_tokens:
  print(s)
  parsed = p1(s)
  print(str(parsed), str(expected))
  assert(parsed.val == expected)
