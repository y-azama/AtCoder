"""
Created by Y.Azama 2024-07-20
Ref: https://atcoder.jp/contests/abc201/tasks/abc203_b
"""
N, K = map(int, input().split())
ans = N * K * (K + 1) // 2 + K * 100 * N * (N + 1) // 2
print(ans)
