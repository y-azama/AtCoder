"""
Created by Y.Azama 2024-12-21
Ref: https://atcoder.jp/contests/abc385/tasks/abc385_a
"""
a, b, c = map(int, input().split())
ans = 'No'
if a == b+c:
  ans = 'Yes'
if b == c+a:
  ans = 'Yes'
if c == a+b:
  ans = 'Yes'
if a == b and b == c:
  ans = 'Yes'

print(ans)