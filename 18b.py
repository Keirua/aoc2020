import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/18.txt', 'r') 
data = [i.strip().replace(" ", "") for i in file.readlines()]

class Nb:
  def __init__(self, v):
    self.val = v

  def __truediv__(self, other):
    return Nb(self.val + other.val)

  def __sub__(self, other):
    return Nb(self.val * other.val)

  def __repr__(self):
    return str(self.val)


def p2(expr):
  expr = re.sub("(\d+)", "Nb(\\1)", expr).replace("*", "-").replace("+", "/")
  return eval(expr)

sample_tokens_p2 = [
  ("2 * 3 + (4 * 5)", 46),
  ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
  ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
  ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340)
]
for s,expected in sample_tokens_p2:
  print(s)
  parsed = p2(s)
  print(str(parsed), str(expected))
  assert(parsed.val == expected)


print(sum(map(lambda e: p2(e).val, data)))