def announce(f):
    def wrapper():
        print("About to run a function...")
        f()
        print("Donde with function")
    return wrapper


@announce
def hello():
    print("Hello, world!")
    
hello()