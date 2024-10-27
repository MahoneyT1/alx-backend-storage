def abc(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        result = func(*args, **kwargs)
        print(result)
    return wrapper
    

@abc
def num(arg):
    return arg * arg

ans = num(5)
