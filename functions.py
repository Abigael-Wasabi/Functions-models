def maximum_of_numbers():
    maximum = max(10, 20)
    return maximum


result = maximum_of_numbers()
print(result)


def maximum_of_numbers():
    c = input("first_number: ")
    d = input("second_number: ")
    e = max(c, d)
    print(e)


maximum_of_numbers()


def maximum_of_numbers(a, b):
    print(max(a, b))


maximum_of_numbers(10, 20)


def fizz_buzz(h):
    if h % 3 == 0:
        print("fizz")
    elif h % 5 == 0:
        print("buzz")
    elif h % 3 and h % 5 == 0:
        print("fizzbuzz")
    else:
        print(h)


print(fizz_buzz(45))


def speed_of_drivers(speed):
    if speed < 70:
        print("ok")
    elif speed > 70:
        speedy = input("speed: ")
        k = (int(speedy)-70)/5
        print("k")
        if k > 12:
            print("licence suspended")


speed_of_drivers(100)
