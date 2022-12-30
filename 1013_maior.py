# -*- coding: utf-8 -*-

a, b, c = (int(x) for x in input().split())

mab = (a + b + abs(a-b))/2
mabc = int((mab + c + abs(mab - c))/2)

print("{} eh o maior".format(mabc))