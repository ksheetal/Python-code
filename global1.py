a=4
def f():
    a=5
    def g():
        b=a
        print("inside funtion g : ","a=",a,"b=",b)
        a=5
    g()
f()
