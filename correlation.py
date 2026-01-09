import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# 1. ხელით ამოწერილი მონაცემები
x_values = np.array([-8.9, -6.7, -4.0, -2.0, 1.0, 2.6, 4.5, 6.0, 8.9])
y_values = np.array([-7.0, -5.0, -2.0, 0.8, 1.0, 3.0, 4.0, 6.5, 8.0])

# 2. კორელაციის გამოთვლა
r = np.corrcoef(x_values, y_values)[0, 1]
print(f"Pearson's Correlation Coefficient (r): {r:.4f}")

# 3. გრაფიკის აგება
plt.figure(figsize=(10, 8))
plt.scatter(y_values, x_values, color='blue', s=100, label='Data Points', alpha=0.6)

# ტრენდის ხაზის (რეგრესია)
m, b = np.polyfit(y_values, x_values, 1)
plt.plot(y_values, m*y_values + b, color='red', label=f'Trend Line (r={r:.4f})')

plt.xlabel("Y ღერძი", fontsize=12)
plt.ylabel("X ღერძი", fontsize=12)


plt.title("Pearson Correlation Analysis (Source Layout)", fontsize=14)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

# 4. შენახვა
plt.savefig('correlation_graph.png')
print("სურათი შენახულია!")