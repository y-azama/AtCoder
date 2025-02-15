"""
Created by Y.Azama 2025-02-15
Ref: https://atcoder.jp/contests/abc393/tasks/abc393_b
"""
S = list(input())
a = []
b = []
c = []
for i, s in enumerate(S):
  if s == 'A': a.append(i)
  if s == 'B': b.append(i)
  if s == 'C': c.append(i)

ans = 0
for i in a:
  for j in b:
    for k in c:
      if i > j or j > k: continue
      if j-i == k-j: ans += 1
print(ans)