import time

def debug(func):
    def wrapper(*args,**kwargs):
        args_value= ', '.join(str(arg) for arg in args)
        kwargs_value=', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f'{func.__name__} with {args_value} args and {kwargs_value} kwargs')
        return func(*args,**kwargs)
    return wrapper


def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@debug
@timer
def example(n):
    time.sleep(n)
example(2)

@debug
def greet(name,greeting='hello'):
    print( f'{name} ,{greeting}')
greet('neha',greeting='hanji')