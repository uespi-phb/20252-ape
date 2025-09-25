
def f(a,b,*c,**d):
    print('a:',a)
    print('b:',b)
    print('c:',c)
    print('d:',d)
    print('--------')
    
f(1,2)
f(1,2,4,5)
f(1,2,4,5,x=10,y=20)

