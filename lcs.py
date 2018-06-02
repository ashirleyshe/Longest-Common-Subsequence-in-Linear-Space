# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:00:15 2017

@author: ashirley
"""

def clens(x, y):
    now = [0] * (len(y) + 1)    # now dealing with
    pre = [0] * (len(y) + 1)    # previous one
    for xs in x:
        for i, ys in enumerate(y):
            if xs == ys:
                now[i + 1] = pre[i] + 1
            else:
                now[i + 1] = max(now[i], pre[i + 1])
        pre = now[:]
    return now

def lcs(x, y):
    Xm = len(x)
    Yn = len(y)
    if Xm == 0:
        return []
    if Yn == 0:
        return []
    if Xm == 1:
        return [x[0]] if x[0] in y else []
    if Yn == 1:
        return [y[0]] if y[0] in x else []
    else:
        mid = Xm // 2
        x1 = x[:mid]
        x2 = x[mid:]
        up = clens(x1, y) 
        down = clens(x2[::-1], y[::-1])
        max_sum, k = max((up[i] + down[Yn - i], i) for i in range(Yn + 1))
        y1 = y[:k]
        y2 = y[k:]
        return lcs(x1, y1) + lcs(x2, y2)

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        str_in = [str(i) for i in input().split()]
        x = str_in[0]
        y = str_in[1]
        print(''.join(map(str, lcs(x, y))))