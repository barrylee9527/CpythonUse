# example.pyx
cdef extern from "example.c":
    int add(int a, int b)

def add_numbers(int a, int b):
    return add(a, b)
