"""
Created by Y.Azama 2024-09-28
Ref: https://atcoder.jp/contests/abc373/tasks/abc373_b
"""
S = input()
a = ord('A')
ans = 0
pre_idx = S.index('A')
cur_idx = 0
for i in range(1, 26):
  cur_idx = S.index(chr(a + i))
  ans += abs(pre_idx - cur_idx)
  pre_idx = cur_idx
print(ans)