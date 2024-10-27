"""
Created by Y.Azama 2024-09-21
Ref: https://atcoder.jp/contests/abc372/tasks/abc372_a
"""
S = input()
ans = ''
for i in range(len(S)):
  if S[i] != '.':
    ans += S[i]

print(ans)