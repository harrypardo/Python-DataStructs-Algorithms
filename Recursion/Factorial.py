def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


memo = [1, 2]


def factorial_dynamic(n):
    if n <= 1:
        return memo[0]
    if len(memo) - 1 >= n:
        return memo[n - 1]

    for i in range(len(memo) - 1, n - 1):
        memo.append((i + 2) * memo[i])
    return memo[n - 1]


print(factorial_dynamic(3))
print(memo)

print(factorial_recursive(10))


