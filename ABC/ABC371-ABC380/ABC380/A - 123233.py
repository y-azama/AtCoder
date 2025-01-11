"""
Created by Y.Azama 2024-11-16
Ref: https://atcoder.jp/contests/abc380/tasks/abc380_a
"""
S = input()
ans = 'Yes'
if S.count('1') != 1:
  ans = 'No'
if S.count('2') != 2:
  ans = 'No'
if S.count('3') != 3:
  ans = 'No'
print(ans)