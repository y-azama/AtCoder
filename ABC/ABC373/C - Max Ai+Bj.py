"""
Created by Y.Azama 2024-09-28
Ref: https://atcoder.jp/contests/abc373/tasks/abc373_c
"""
N = int(input())
A = [int(n) for n in input().split()]
B = [int(n) for n in input().split()]
print(max(A) + max(B))