"""
Created by Y.Azama 2024-11-16
Ref: https://atcoder.jp/contests/abc380/tasks/abc380_b
"""
S = input()
ans = []
cnt = 0
for i in range(1, len(S)):
  if S[i] == '|':
    ans.append(cnt)
    cnt = 0
    continue
  cnt += 1
print(*ans)