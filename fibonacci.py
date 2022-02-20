"""
@author: thomastesselaar

Interestingly, as demonstrated below, returing the n-1th index of fibonacciArr 
is faster than resursively finding the nth number
"""
import time

# Generates the nth Fibonacci number
def fibonacciNum(n):
    if (n <= 0) :
        return -1
    if (n == 1 or n == 2) :
        return 1
    return (fibonacciNum(n - 1) + fibonacciNum(n - 2))

# Generates a Fibonacci array of length n
def fibonacciArr(n):
    if (n <= 0) :
        return [-1]
    if (n == 1) :
        return [1]
    arr = [1, 1]
    for i in range(2, n):
        arr.append(arr[i-1] + arr[i-2])
    return arr

# Inefficiently generates an Fibonacci array of length n
def inefficientFibonacciArr(n):
    if (n <= 0) :
        return [-1]
    arr = [1]
    for i in range(2, n+1):
        arr.append(fibonacciNum(i))
    return arr




n = 30
start = time.time()
print(fibonacciNum(n))
end = time.time()
print(end - start)

start = time.time()
print(fibonacciArr(n))
end = time.time()
print(end - start)

start = time.time()
print(inefficientFibonacciArr(n))
end = time.time()
print(end - start)
