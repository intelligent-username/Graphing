import matplotlib.pyplot as plt

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

VR = 20
input_values = range(VR)
output_values = fibonacci(VR)

plt.plot(input_values, output_values, marker='*', linestyle='-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Fibonacci first {VR} numbers')
plt.grid(True)
plt.xticks(range(0, VR, max(1, VR//10)))
plt.show()
