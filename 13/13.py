import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sales = [12000, 15000, 18000, 22000, 25000, 24000, 23000, 21000, 20000, 19000, 16000, 14000]

plt.figure(figsize=(10, 6))

plt.plot(months, sales, marker='o', linestyle='-', color='b', label='Sales Data')

plt.title('Monthly Sales Data for 2023')
plt.xlabel('Months')
plt.ylabel('Sales (in USD)')
plt.grid(True)
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()