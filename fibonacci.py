def generate_fibonacci(n):
    fib_sequence = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers

    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence

# Specify the number of Fibonacci numbers you want to generate
num_terms = 10

# Call the function to generate the Fibonacci sequence
fibonacci_sequence = generate_fibonacci(num_terms)

# Print the generated Fibonacci sequence
print("Fibonacci Sequence:")
print(fibonacci_sequence)
