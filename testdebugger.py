def ticket(passenger_type):
    passenger_type = passenger_type.upper().strip()
    if passenger_type == 'A':
        fare = 50
    elif passenger_type == 'S':
        fare = 45
    elif passenger_type == 'C':
        fare = 25

    return fare


p = input('Passenger type A,C,S,')
print(ticket(p))
