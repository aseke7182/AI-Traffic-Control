f = open("out.txt", "r")

# Read number of cars for each side of road from "out.txt" file
number_of_vehicles = [
    int(f.readline()),
    int(f.readline()),
    int(f.readline()),
    int(f.readline())
]

baseTimer = 120  # Timer
timeLimits = [5, 30]  # Min and Max time for traffic lights

sides = [
    "Abylaikhan st. North-South",
    "Abylaikhan st. South-North",
    "Tole bi st. East-West",
    "Tole bi st. West-East"
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
