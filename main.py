import matplotlib.pyplot as plt

initial_velocity = int(input("Enter the initial velocity: "))
initial_velocity_unit = input("Enter the initial velocity unit: (m/s) or (km/h): For m/s enter 1, for km/h enter 2: ")
if initial_velocity_unit == "1":
    initial_velocity_unit = "m/s"
elif initial_velocity_unit == "2":
    initial_velocity = initial_velocity * 1000 / 3600

final_velocity = int(input("Enter the final velocity: "))
final_velocity_unit = input("Enter the final velocity unit: (m/s) or (km/h): For m/s enter 1, for km/h enter 2: ")
if final_velocity_unit == "1":
    final_velocity_unit = "m/s"
elif final_velocity_unit == "2":
    final_velocity = final_velocity * 1000 / 3600

print(initial_velocity, initial_velocity_unit)
print(final_velocity, final_velocity_unit)
acceleration = int(input("Enter the acceleration: "))
acceleration_unit = input("Enter the acceleration unit: (m/s^2) or (km/h^2): For m/s^2 enter 1, for km/h^2 enter 2: ")
if acceleration_unit == "1":
    acceleration_unit = "m/s^2"
elif acceleration_unit == "2":
    acceleration_unit = acceleration * 1000 / 129600


time = int(input("Enter the time: (in seconds) "))

distance = 1/2 * acceleration * time**2 + initial_velocity * time
print(distance)

# Define data points
y = [initial_velocity, initial_velocity + 2, initial_velocity + 3, initial_velocity + 4, initial_velocity + 5, final_velocity]
x = [time, time + 2, time + 3, time + 4, time + 5, time + 6]



plt.plot(x, y)
plt.show()
