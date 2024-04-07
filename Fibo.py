import matplotlib.pyplot as plt
import argparse

# Function to read Fibonacci numbers from the file
def read_fibonacci(file_path, n):
    with open(file_path, 'r') as file:
        fib_numbers = [int(line.strip()) for line in file.readlines()[:n]]
    return fib_numbers

# Setup command line argument parsing
parser = argparse.ArgumentParser(description="Plot Fibonacci numbers.")
parser.add_argument("num_values", nargs='?', default=20, type=int, help="Number of Fibonacci values to plot")
args = parser.parse_args()

# Ensure number of values does not exceed 10,000
VR = max(1, min(args.num_values, 10000))

# Read pre-generated Fibonacci numbers
fibonacci_values = read_fibonacci('Storage/10_000_fibo.txt', VR)

# Plotting
input_values = range(VR)
plt.plot(input_values, fibonacci_values, marker='x', linestyle='-')
plt.xlabel("Index")
plt.ylabel("Fibonacci Value")
plt.title(f"Fibonacci's first {VR} numbers")
plt.grid(True)
plt.xticks(range(0, VR, max(1, VR//10)))
# plt.savefig(fr'/Graphs/Fibonacci/first_{VR}.pdf') some glitch with savefig, fix later or nto depending on if I need it (Not that 'Graphs' folder doesn't exist)
print("Note: usage is \npython Fibo.py [num_values]\n where num_values is 20 by default")

plt.show()

