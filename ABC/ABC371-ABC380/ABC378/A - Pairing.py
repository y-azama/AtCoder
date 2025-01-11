"""
Created by Y.Azama 2024-11-02
Ref: https://atcoder.jp/contests/abc378/tasks/abc378_a
"""
A = [int(n) for n in input().split()]
cnt = [0,0,0,0]
ans = 0
for a in A:
  cnt[a-1] += 1
for c in cnt:
  ans += c // 2
print(ans)