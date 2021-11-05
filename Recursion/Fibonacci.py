def fibonacci_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)


memo = [0, 1]


def fibonacci_dynamic(n):
    if n <= 0:
        return memo[0]
    if len(memo) - 1 >= n:
        return memo[n]

    for i in range(len(memo) - 1, n):
        memo.append(memo[i] + memo[i - 1])
    return memo[n]


print(fibonacci_dynamic(10))
print(memo)

print(fibonacci_recursive(10))


