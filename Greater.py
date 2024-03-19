x = 6
y = 5
c = 56
a = 60
if x>y and x>c and x>a:
    print("x is the greatest number")
elif y>x and y>c and y>a:
    print("y is the greatest number")
elif c>x and c>y and c>a:
    print("c is the greatest number")
else:
    print("a is the greatest number")

if x<y and x<c and x<a:
    print(x)
    if y<c and y<a:
        print(y)
    elif c<a:
        print(c)
        print(a)
    else:
        print(a)
        print(c)
elif y<x and y<c and y<a:
    print(y)
    if x<c and x<a:
        print(x)
    elif c<a:
       print(c)
       print(a)
    else:
       print(a)
       print(c)
elif c<x and c<y and c<a:
    print(c)
    if a<x and a<y:
        print(a)
    elif x<y:
        print(x)
        print(y)
    else:
        print(y)
        print(x)
else:
    print(a)
    if c<y and c<x:
        print(c)
    elif y<x:
        print(y)
        print(x)
    else:
        print(x)
        print(y)

