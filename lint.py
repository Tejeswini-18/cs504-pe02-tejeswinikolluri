"The following code generate and print the Fibonacci numbers from 1 to 10."


def fib(number):
    "the following function returns the nth Fibonacci number."
    if number in (0, 1):
        return number
    return fib(number - 1) + fib(number - 2)


def print_fib_sequence():
    "the following function Print the Fibonacci numbers from 1 to 10."""
    for i in range(1, 11):
        print(f"i: {i} fib: {fib(i - 1)}")

print("Fibonacci from 1 to 10:")
print_fib_sequence()
