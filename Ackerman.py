import matplotlib.pyplot as plt
import numpy as np

# The Ackermann function
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Recursive Fibonacci function
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Values
m_values = range(0, 4)  # Be very careful with larger values due to computational complexity
n_values = range(0, 11)  # Adjust based on computational resources

# Plot setup
fig, ax = plt.subplots()

# Plotting Ackermann values for different m
for m in m_values:
    ack_values = [ackermann(m, n) for n in n_values if ackermann(m, n) < 2**16]  # Limit values for visibility
    ax.plot(n_values[:len(ack_values)], ack_values, label=f'Ackermann m={m}', marker='o')

# Adding Fibonacci sequence curve
fib_values = [fibonacci(n) for n in n_values]
ax.plot(n_values, fib_values, label='Fibonacci', linestyle='--', color='k')

# Additional plot settings
ax.set_xlabel('n')
ax.set_ylabel('Function Values')
ax.set_yscale('log')  # Logarithmic scale due to differing growth rates
ax.legend()
plt.title('Ackermann Function vs. Fibonacci Sequence')
plt.grid(True)

plt.show()
