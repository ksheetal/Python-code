def func(bar=[]):
    bar.append('xyz')
    return bar
print (func())

def func(bar=[]):
    bar.extend('xyz')
    return bar
print(func())
