import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = []

for day in days:
    temp = float(input(f"Enter temperature for {day}: "))
    temperatures.append(temp)

plt.plot(days, temperatures, marker="o", linestyle="-", color="b")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variations Over a Week")
plt.show()
