import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data
data = [12, 15, 14, 10, 18, 20, 22, 15, 17, 19, 16, 14, 13, 15, 18]

# ----- Scatter Plot -----
plt.figure(figsize=(10, 4))
plt.scatter(range(len(data)), data, color='blue', marker='o')
plt.title('Scatter Plot of Data')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()

# ----- Heat Map -----
# Convert data into 2D array for heatmap (5x3 example)
heat_data = np.array(data[:15]).reshape(5, 3)

plt.figure(figsize=(6, 5))
sns.heatmap(heat_data, annot=True, cmap='coolwarm')
plt.title('Heat Map of Data')
plt.show()
