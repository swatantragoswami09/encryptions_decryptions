c=0
def f(t,n):
    global c
    if n==1:
        return t
    else:
        c+=1
        return f(t*2+c,n-1)
        
print(f(7,int(input())))
