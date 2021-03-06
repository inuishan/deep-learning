import numpy as np
import time


def vectorization_faster_example_1():
    a = np.random.rand(1000000)
    b = np.random.rand(1000000)
    tic = time.time()
    c = np.dot(a, b)
    toc = time.time()
    print("vectorized")
    vectorized_time = (toc - tic) * 1000
    print(str(vectorized_time) + "ms")
    c = 0
    tic = time.time()
    for i in range(1000000):
        c += a[i] * b[i]
    toc = time.time()
    print("non vectorized")
    non_vectorized_time = (toc - tic) * 1000
    print(str(non_vectorized_time) + "ms")
    print("vectorized ran " + str(non_vectorized_time / vectorized_time) + " times faster!")


# vectorization_faster_example_1()

def numpy_method_examples():
    a = np.random.rand(1000000)
    print(a.shape)
    exp = np.exp(a)
    print(exp.shape)
    log = np.log(a)
    max = np.max(a, 0)
    print(a)
    # element wise square
    print(a ** 2)
    # element wise inverse
    print(1 / a)


numpy_method_examples()
