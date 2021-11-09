# fibo(n) = fibo(n-2) + fibo(n-1)
# fibo(0) = 0
# fibo(1) = 1

def fibo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-2) + fibo(n-1)

# -----------------------------------------------------------------
print(fibo(3))
