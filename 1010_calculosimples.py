# -*- coding: utf-8 -*-

p1 = input().split()
p2 = input().split()
total = int(p1[1]) * float(p1[2])
total += int(p2[1]) * float(p2[2])

print("VALOR A PAGAR: R$ {:.2f}".format(total))
