import matplotlib.pyplot as plt #type: ignore
import argparse

# Function to read Fibonacci numbers from the file
def read_fibonacci(file_path, n):
    with open(file_path, 'r') as file:
        fib_numbers = [int(line.strip()) for line in file.readlines()[:n]]
    return fib_numbers

# Setup command line argument parsing
parser = argparse.ArgumentParser(description="Plot the Fibonacci Sequence.")
parser.add_argument("num_values", nargs='?', default=20, type=int, help="Number of Fibonacci values to plot (1-10,000)")
args = parser.parse_args()

# Ensure number of values does not exceed 10,000
VR = max(1, min(args.num_values, 10000))

# Read pre-generated Fibonacci numbers
fibonacci_values = read_fibonacci('Storage/10_000_fibo.txt', VR)

# Plotting
input_values = range(VR)
plt.figure(figsize=(12, 8))  # Increase the figure size
plt.plot(input_values, fibonacci_values, marker='o', linestyle='-', color='#1f77b4', linewidth=2, markersize=8)
plt.xlabel("Index", fontsize=14)
plt.ylabel("Fibonacci Value", fontsize=14)
plt.title("Fibonacci Sequence: First N Numbers", fontsize=18, fontweight='bold', pad=20)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(range(0, VR, max(1, VR//10)), fontsize=12)
plt.yticks(fontsize=12)

# Add annotations
plt.annotate("Rapid growth of Fibonacci numbers", xy=(VR-5, fibonacci_values[-5]), xytext=(VR-10, fibonacci_values[-2]),
             arrowprops=dict(arrowstyle="->", color='#d62728'))

# Add a legend
plt.legend(['Fibonacci Sequence'], loc='upper left', fontsize=12)

# Save the plot (uncomment if needed)
# plt.savefig(fr'/Graphs/Fibonacci/first_{VR}.pdf')

print(f"Note: Usage is 'python Fibo.py [num_values]' where num_values is between 1 and 10,000 (default is 20).")
plt.show()
