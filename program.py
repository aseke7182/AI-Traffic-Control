f = open("out.txt", "r")

# Read number of cars for each side of road from "out.txt" file
number_of_vehicles_in_four = [
    int(f.readline()),
    int(f.readline()),
    int(f.readline()),
    int(f.readline())
]
number_of_vehicles = [
    int(number_of_vehicles_in_four[0]) + int(number_of_vehicles_in_four[1]),
    int(number_of_vehicles_in_four[2]) + int(number_of_vehicles_in_four[3])
]

baseTimer = 120  # Timer
timeLimits = [5, 60]  # Min and Max time for traffic lights

sides = [
    "Abylaikhan st.",
    "Tole bi st."
]

for i in range(len(sides)):
    print("number of cars on ", sides[i], ": ", number_of_vehicles[i])

times = [
    (i / sum(number_of_vehicles)) * baseTimer
    if timeLimits[0] < (i / sum(number_of_vehicles)) * baseTimer < timeLimits[1]
    else min(timeLimits, key=lambda x: abs(x - (i / sum(number_of_vehicles)) * baseTimer))
    for i in number_of_vehicles
]

print()

for i in range(len(sides)):
    print("Seconds for ", sides[i], ": ", times[i])

print("Total waiting time: ", sum(times))
