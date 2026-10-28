import time

def cache(func):
    cache_value = {}
    print("Cache initialized:", cache_value)
    
    def wrapper(*args):
        if args in cache_value:
            print("Fetching from cache...")
            return cache_value[args]  # ⚡ Added return here!
            
        # This only runs if args were NOT in the cache
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_func(a, b):
    time.sleep(4)
    return a + b

# ⏳ First call: Takes 4 seconds, prints "Cache initialized" once, then calculates.
print("Result 1:", long_running_func(2, 4))

# ⚡ Second call: Runs INSTANTLY because it returns early from the cache.
print("Result 2:", long_running_func(2, 4))
