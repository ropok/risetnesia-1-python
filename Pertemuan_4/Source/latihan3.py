# def count_paths(n, m):
#     if n == 1 or m == 1:
#         return 1
#     return count_paths(n-1, m) + count_paths(n, m-1)

# n, m = 5, 5
# print(count_paths(n, m))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))

# 0,1,1,2,3,5