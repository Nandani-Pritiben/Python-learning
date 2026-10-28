x=99
def func(num):
    def actual(x):
        return x**num
    return actual

f=func(3)
g=func(2)

print(func(5))
print(f(3))
print(g(2))