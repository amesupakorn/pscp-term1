""" Nearer """
def main():
    """ Nearer """
    alice, bob, car = int(input()), int(input()), int(input())
    car_alice = abs(car-alice)
    car_bob = abs(car-bob)
    if car_alice == car_bob:
        print("%s %d" %("Sundaes", car_alice))
    elif car_alice > car_bob:
        print("%s %d" %("Bob", car_bob))
    elif car_bob > car_alice:
        print("%s %d" %("Alice", car_alice))
main()
