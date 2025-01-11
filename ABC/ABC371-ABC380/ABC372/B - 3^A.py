"""
Created by Y.Azama 2024-09-21
Ref: https://atcoder.jp/contests/abc372/tasks/abc372_b
"""
M = int(input())

pow3 = []
for i in range(11):
  pow3.append(3**i)

ans = []
while M > 0:
  idx = max([i for i, x in enumerate(pow3) if x <= M])
  ans.append(idx)
  M -= pow3[idx]
  
print(len(ans))
print(*ans)