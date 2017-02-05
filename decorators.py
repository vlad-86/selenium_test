import time



# Example one
def timer(func):
    def tmp(*args):
        t = time.time()
        result = func(*args)
        print('Time taken to calculate - {0}'.format(time.time()-t))
        return result
    return tmp


@timer
def sum1(x, y):
    return time.sleep(1)

sum1(1, 2)

# Example two
def my_decorator(f):
    def wrapper():
        print('do smth Before initial function call')
        f()
        print('do smth After initial function call')

    return wrapper

@my_decorator
def main_func():
    print('Inside main function')

main_func()