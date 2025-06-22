
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 185
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 290
    elif city == "Los Angeles":
        return 475
    else:
        return 0
    
def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days
    
def trip_cost(city, days, money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + money

print("cost of car rental: ", rental_car_cost(6))

print("Cost of plane ride: ",plane_ride_cost("Los Angeles"))

print("Cost of hotel room: ", hotel_cost(7))

print("Total cost of the trip:",trip_cost("Los Angeles",7,500))

print(trip_cost("Tampa",6,500))