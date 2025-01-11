"""
Created by Y.Azama 2024-07-01
Ref: https://atcoder.jp/contests/abc360/tasks/abc360_a
"""
import re

S = input()
if S.find('R') < S.find('M'):
  print('Yes')
else:
  print('No')