def print_hello():
    print("안녕?")

def call_10_times(func):
    for i in range(10):
        func()

call_10_times(print_hello)