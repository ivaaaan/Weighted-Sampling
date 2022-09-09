import random
import numpy

def sample(elements, k):
  res = []
  for e in elements:
    r = random.uniform(0, 1)
    i = (-1 * numpy.log1p(r * -1)) / e[0]
    res.append((e[0], e[1], i))
    res.sort(key=lambda x: x[2])
    res = res[0:k]
  return res


stream = [(50, "ivan"), (30, "dima"), (25, "andew"), (1, "denis"), (24, "alik")]
stats = {}

for i in range(1000):
  s = sample(stream, 1)[0]
  if s[1] in stats:
    stats[s[1]]+=1
  else:
    stats[s[1]] = 1
s = []
for k, v in stats.items():
  s.append((k, v))

s.sort(key=lambda x: x[1], reverse=True)
print(s)