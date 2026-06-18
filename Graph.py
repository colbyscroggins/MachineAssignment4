import matplotlib.pyplot as plt
import numpy as np

# Known Derivative
x = 1.0
known_derivative = np.cos(x)

# h Values from 1/2 to 1/2^30
i_values = np.arange(1, 31)
h_values = 2.0 ** (-i_values)

# Calculate Approximate Derivatives and Absolute Errors
approx_derivative = (np.sin(x + h_values) - np.sin(x)) / h_values
abs_error = np.abs(approx_derivative - known_derivative)

# Plotting the results
plt.figure(figsize=(9, 6))
plt.plot(h_values, abs_error, marker='o', linestyle='-', color='b', markersize=4)
plt.xscale('log')
plt.yscale('log')

plt.title("h vs. Absolute Error (Log Scale)")
plt.xlabel("h")
plt.ylabel("Abs. Error")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.gca().invert_xaxis()

plt.show()