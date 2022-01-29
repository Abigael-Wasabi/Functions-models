def maximumofnumbers(a, b):
    return(max(a, b))


def fizz_buzz(h):
    if h % 3 and h % 5 == 0:
        print("fizzbuzz")
    elif h % 3 == 0:
        print("fizz")
    elif h % 5 == 0:
        print("buzz")
    else:
        print(h)


def speed_of_drivers(speed):
    if speed < 70:
        print("ok")
    elif speed > 70:
        speedy = input("speed: ")
        k = (int(speedy)-70)/5
        print(k)
        if k > 12:
            print("licence suspended")


def show_numbers():
    for i in range(0, 21):
        if i % 2 == 0:
            print(i, "EVEN")
        elif i % 2 != 0:
            print(i, "ODD")
