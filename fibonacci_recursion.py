def fibonacci(n):
    # Write your code here.
    twobehind = 0
    behind = 1
    i = 0
    while i < (n - 1):
        current = twobehind + behind
        twobehind = behind
        behind = current
        i = i + 1
    if (n == 0) or (n == 1):
        return n
    return current
    
    
n = int(raw_input())
print(fibonacci(n))