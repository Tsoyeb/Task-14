# calculate the total cost of a holiday

# Defines the cost of the flight depending on location.
def get_price(city_flight):
    if city_flight.lower() == 'london':
        plane_cost = 250
    elif city_flight.lower() =='manchester':
        plane_cost = 300
    elif city_flight.lower() == 'bristol':
        plane_cost = 120
    elif city_flight.lower() == 'edinburgh':
        plane_cost = 500
    return plane_cost

# Defines total hotel cost by multiplying the number of nights by 150.
def get_cost_per_night(num_nights):
    hotel_cost= 150 * num_nights
    return hotel_cost

# Defines total car rental cost by multiplying the number of days by 120.
def get_rental_cost(rental_days):
    car_rental = 120 * rental_days
    return car_rental

# Defines holiday cost by adding all the total values together.
def get_holiday_cost():
    holiday_cost = hotel_cost + plane_cost+  car_rental
    return holiday_cost
    
# The while loop takes in all the input from the user and returns the cost. They will also be prompted if they make a mistake. 
while True:
    city_flight = input('Please enter the destination of the city you wish to fly to.\n(flights are currently only available to London, Manchester, Bristol, Edinburgh)\n') 
    if city_flight.lower() in ['london', 'manchester', 'bristol', 'edinburgh']:
        print(f'You have chosen {city_flight.capitalize()}')
        plane_cost = get_price(city_flight)
            
    else:
        print('Sorry there are no flights currently to your destination ')
        continue 
    print(f'The cost of your flight is: £{plane_cost}' )

    try:
        num_nights = int(input('Please enter the duration of your stay: '))
    except ValueError:
            print('Oops! Incorrect input, please start again')
            continue
    hotel_cost = get_cost_per_night(num_nights)
    print (f'The total hotel cost is: £{hotel_cost}')

    try:
        rental_days = int(input('Please enter the duration you would like to rent a car for: '))
    except ValueError:
            print('Oops! Incorrect input, please start again')
            continue
    car_rental = get_rental_cost(rental_days)
    print (f'The total car rental cost is: £{car_rental}')
    
    holiday_cost = get_holiday_cost() 
    print(f'The total cost of your holiday is: £{holiday_cost}')
    break
