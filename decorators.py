import time


def timer(func):
    def tmp(*args):
        t = time.time()
        result = func(*args)
        print('Time taken to calculate - {0}'.format(time.time()-t))
        return result
    return tmp


@timer
def sum1(x, y):
    return time.sleep(3)

sum1(1, 2)