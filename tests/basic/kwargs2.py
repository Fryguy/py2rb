def myfunc(a, b, *c, fuga='hoge', **d):
    print(a)
    print(b)
    for i in c:
        print(i)
    print(fuga)
    keys = list(d.keys())
    keys.sort()
    for i in keys:
        print(i)
        print(d[i])

myfunc(1, 2, bar='a', foo='c')
print()
myfunc(1, 2, 3, 4, bar='a', foo='c')
myfunc(1, 2, 3, 4, bar='a', fuga='hogehoge', foo='c')
