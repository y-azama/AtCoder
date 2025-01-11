"""
Created by Y.Azama 2024-08-03
Ref: https://atcoder.jp/contests/abc365/tasks/abc365_b
"""
N = int(input())
A = [[i,int(n)] for i, n in enumerate(input().split())]
A = sorted(A, key=lambda x: x[1])
print(A[-2][0] + 1)