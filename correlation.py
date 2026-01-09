import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# ხელით შეყვანილი მონაცემები
x = np.array([-8.9, -6.7, -4.0, -2.0, 1.0, 2.6, 4.5, 6.0, 8.9])
y = np.array([-7.0, -5.0, -2.0, 0.8, 1.0, 3.0, 4.0, 6.5, 8.0])

# 1. Pearson-ის კორელაციის გამოთვლა
r = np.corrcoef(x, y)[0, 1]
print(f"Pearson's Correlation Coefficient (r): {r:.4f}")

# 2. გრაფიკის აგება
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', s=100, label='Data Points')

# ტრენდის ხაზი
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red', label=f'Trend Line (r={r:.4f})')

plt.title("Pearson Correlation Analysis", fontsize=14)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# 3. შენახვა
plt.savefig('correlation_graph.png')
print("სურათი წარმატებით შეინახა: correlation_graph.png")