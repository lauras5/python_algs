def recur_fibo(n: int) -> int:
    return n if n <= 1 else (recur_fibo(n - 1) + recur_fibo(n - 2))


if __name__ == '__main__':
    print(recur_fibo(5))
