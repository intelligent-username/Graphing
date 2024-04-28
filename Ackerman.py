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
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting Ackermann values for different m
line_styles = ['-', '--', ':', '-.']
for i, m in enumerate(m_values):
    ack_values = [ackermann(m, n) for n in n_values if ackermann(m, n) < 2**16]  # Limit values for visibility
    ax.plot(n_values[:len(ack_values)], ack_values, label=f'Ackermann m={m}', linestyle=line_styles[i], linewidth=2)

# Adding Fibonacci sequence curve
fib_values = [fibonacci(n) for n in n_values]
ax.plot(n_values, fib_values, label='Fibonacci', linestyle='--', color='k', linewidth=2)

# Additional plot settings
ax.set_xlabel('n')
ax.set_ylabel('Function Values')
ax.set_yscale('log')  # Logarithmic scale due to differing growth rates
ax.legend()
ax.set_title('Ackermann Function vs. Fibonacci Sequence', fontsize=16)
ax.grid(True, linestyle='--', alpha=0.5)
plt.show()
