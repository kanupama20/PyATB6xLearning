import time

def time_decorator(func):
    def wrapper():
        start_time= time.time()
        func()
        end_time= time.time()
        total_time = end_time - start_time
        print("Total time taken by test case :", total_time)
    return wrapper

def log_decorator(func):
    def wrapper():
        func()
        print("Logs of the test case")
    return wrapper


@time_decorator
def test_case1() :
    time.sleep(3)
    print("This is test case 1")

@log_decorator
def test_case2():
    time.sleep(2)
    print("This is test case 2")

test_case1()
test_case2()
