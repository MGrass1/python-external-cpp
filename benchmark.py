from ctypes import cdll
import math
import time
lib = cdll.LoadLibrary("./custom_cpp/primes.dll")


def is_prime(some_int):
    if some_int < 2:
        return False
    elif some_int == 2:
        return True
    else:
        for real_int in range(2, math.ceil(math.sqrt(some_int))+1):
            if some_int % real_int == 0:
                return False
    return True


max_count = 1000000
prime_list_py = list()
py_start = time.clock()
for target_int in range(2, max_count):
    is_prime(target_int)
py_total = time.clock() - py_start


prime_list_cpp = list()
cpp_start = time.clock()
for target_int in range(2, max_count):
    lib.cpp_is_prime(target_int)
cpp_total = time.clock() - cpp_start

assert len(prime_list_cpp) == len(prime_list_py)

print("Python took %s seconds\nCpp took %s seconds" % (py_total, cpp_total))
print("Cpp libraries are %s times faster for prime calculations.\n" % (py_total/cpp_total,))
