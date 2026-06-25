import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
sales = [120, 150, 180, 170, 200, 220, 250]

plt.plot(days, sales, marker='o')
plt.title("Daily Sales Trend")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.grid(True)

plt.show()    