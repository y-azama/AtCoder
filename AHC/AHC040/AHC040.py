import random

def query(prdb):
  print(len(prdb))
  for p, r, d, b in prdb:
    print(p, r, d, b)
  W, H = map(int, input().split())
  return W, H

def random_r(wh, edge, start):
  ret = []
  w = 0
  for i in range(start, len(wh)):
    r = random.randrange(2)
    if w + wh[i][r] > edge: break

    w += wh[i][r]
    ret.append([r, wh[i]])
  return ret

def calc_shape(rr):
  ret = []
  w = 0
  for r, s in rr:
    ret.append([w, s[r-1]])
    w += s[r]
  ret.append([w,0])
  return ret

def merge_shape(shape, _shape):
  if len(shape) == 0: return _shape

  ret = []
  idx = 0
  w = 0
  h = 0
  for i in range(1, len(_shape)):
    s = _shape[i]
    while idx < len(shape):
      if s[0] >= shape[idx][0]: break

      h = max(h, shape[idx][1])
      idx += 1
    ret.append([w,h+_shape[i-1][1]])
    w += s[0]
    h = shape[idx-1][1]
  
  if idx == len(shape):
    ret.append([w,0])
    return ret
  
  for s in shape[idx:]:
    ret.append(s)
  return ret

N, T, sigma = map(int, input().split())
wh = []
area = []
for _ in range(N):
  w, h = map(int, input().split())
  wh.append([w, h])
  area.append(w * h)

edge = int((1.1 * sum(area)) ** (1/2))

score = -1
rr = []
for t in range(T):
  prdb = []
  idx = 0
  shape = []
  _rr = []
  for _ in range(1):
    while len(rr) < N:
      tmp = random_r(wh, edge, idx)
      _rr += tmp
      idx = len(_rr)

      _shape = calc_shape(_rr)
      shape = merge_shape(shape, _shape)

    w = shape[-1][0]
    h = max(shape, key=lambda x: x[1])
    if score < 0:
      score = w + h
      rr = _rr.copy()
      break
    elif score > w + h:
      rr = _rr.copy()
      break

  w = 0
  R = [item[0] for item in rr]
  for i, r in enumerate(R):
    b = -1 if w + wh[i][r] > edge else i-1
    prdb.append((
      i,
      r,
      'U',
      b
      ))
    
    if w + wh[i][r] > edge: w = 0
    w += wh[i][r]
  query(prdb)
