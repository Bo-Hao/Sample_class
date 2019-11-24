

def it():
    a, b = 0, 1
    while a < 100:
        yield a
        a, b = b, a+b 
        





if __name__ == "__main__":
    f = it()
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
