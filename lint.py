"""Generate and print the first ten Fibonacci numbers."""


def fib(number):
    """Return the nth Fibonacci number."""
    if number in (0, 1):
        return number
    return fib(number - 1) + fib(number - 2)


def print_fib_sequence():
    """Print the first ten Fibonacci numbers."""
    for i in range(1, 11):
        print(f"i: {i} fib: {fib(i - 1)}")

print("Fibonacci from 1 to 10:")
print_fib_sequence()
