location = input("Where are you going?")
distance = int(input("How far is it in kilometers?"))

# in km/h
speed_by_bike = 20
speed_by_train = 150
speed_by_bus = 70
speed_by_car = 85

# in hours
travel_time_by_bike = distance/speed_by_bike
travel_time_by_train = distance/speed_by_train
travel_time_by_bus = distance/speed_by_bus
travel_time_by_car = distance/speed_by_car

departure = int(input("What is your departure time (in hours 0-23)?"))

bike_arrival = round(travel_time_by_bike)% 24
train_arrival = round(travel_time_by_train)% 24
bus_arrival = round(travel_time_by_bus)% 24
car_arrival = round(travel_time_by_car)% 24

print("Travel time in hours is", round(travel_time_by_bike, 2), "and your arrival time at", location, "by bus is approximately:", bike_arrival)
print("Travel time in hours is", round(travel_time_by_train, 2), "and your arrival time at", location, "by train is approximately:", train_arrival)
print("Travel time in hours is", round(travel_time_by_bus, 2), "and your arrival time at", location, "by bus is approximately:", bus_arrival)
print("Travel time in hours is", round(travel_time_by_car, 2), "and your arrival time at", location, "by car is approximately:", car_arrival)
