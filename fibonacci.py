def fibonacci(n):
    fib_seq = []
    a, b = 0, 1
    for _ in range(n):
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq
num_terms = int(input("Enter the number of Fibonacci terms to display: "))
result = fibonacci(num_terms)
print("Fibonacci sequence:", result)

