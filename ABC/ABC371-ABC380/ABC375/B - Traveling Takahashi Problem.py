"""
Created by Y.Azama 2024-10-12
Ref: https://atcoder.jp/contests/abc375/tasks/abc375_b
"""
N = int(input())
ans = 0
x1, y1 = 0, 0
for _ in range(N):
  x2, y2 = map(int, input().split())
  ans += ((x1-x2)**2 + (y1-y2)**2)**(1/2)
  x1 = x2
  y1 = y2
ans += ((x1-0)**2 + (y1-0)**2)**(1/2)
print(ans)