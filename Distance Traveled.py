CAR_DISTANCE_TRAVELED = 70
AN_HOUR = 1
SIX_HOUR = 6
TEN_HOUR = 10
FIFTEEN_HOUR = 15
speed = CAR_DISTANCE_TRAVELED / AN_HOUR
distance_6h = speed * SIX_HOUR
distance_10h = speed * TEN_HOUR
distance_15h = speed * FIFTEEN_HOUR

print(f"The distance the car will travel in 6 hours: {distance_6h}mph")
print(f"The distance the car will travel in 10 hours: {distance_10h}mph")
print(f"The distance the car will travel in 15 hours: {distance_15h}mph")
