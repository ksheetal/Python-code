def func(bar = []):
    bar.append('xyz')
    return bar

print(func())
print(func())
print(func())
