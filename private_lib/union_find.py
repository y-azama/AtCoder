"""
union find
https://note.nkmk.me/python-union-find/
"""
from collections import defaultdict
class UnionFind():
  def __init__(self, N):
    self.parents = [-1] * N
    self.n = N
  
  def find_root(self, x):
    if self.parents[x] < 0: return x

    self.parents[x] = self.find_root(self.parents[x])
    return self.parents[x]
  
  def union(self, x, y):
    x = self.find_root(x)
    y = self.find_root(y)

    if x == y: return

    if x > y:
      x, y = y, x
    
    self.parents[x] += self.parents[y]
    self.parents[y] = x
    return
  
  def is_same(self, x, y):
    return self.find_root(x) == self.find_root(y)
  
  def size(self, x):
    return -self.parents[self.find_root(x)]
  
  def members(self, x):
    r = self.find_root(x)
    return [i for i in range(self.n) if self.find_root(i) == r]
  
  def roots(self):
    return [i for i in range(self.n) if self.parents[i] < 0]
  
  def group_count(self):
    return len(self.roots())
  
  def all_groups(self):
    groups = defaultdict(list)
    for x in range(self.n):
      groups[self.find_root(x)].append(x)
    
    return groups