# implement memoization
# keys --> arg to fn, vals --> return value

def fib(n: int, memo={}) -> int:
    if n in memo: 
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


if __name__ == '__main__':
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(50))
