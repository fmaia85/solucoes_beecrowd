# -*- codding utf-8 -*-

t = int(input())

ts = t%60
t = int(t/60)

tm = t%60
th = int(t/60)

print("{}:{}:{}".format(th, tm, ts))