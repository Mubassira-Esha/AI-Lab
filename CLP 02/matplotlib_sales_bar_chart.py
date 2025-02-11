import matplotlib.pyplot as plt

num_days = int(input("Enter the number of days: "))

days = []
temperatures = []

for i in range(num_days):
    day = input(f"Enter day {i+1}: ")
    temp = float(input(f"Enter temperature for {day}: "))
    days.append(day)
    temperatures.append(temp)

plt.figure(figsize=(8, 5))
plt.plot(days, temperatures, marker='o', linestyle='-', color='b', markersize=8, linewidth=2)

plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variations Over a Week")
plt.grid(True)

plt.show()
