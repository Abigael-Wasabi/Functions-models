from functions import maximumofnumbers, fizz_buzz, speed_of_drivers, show_numbers
while True:
    print("operations")
    print("1.maximumofnumbers\n2.fizz_buzz\n3.speed_od_drivers\n4.show_numbers")
    choice = input("choose an operation to run: ")
    if (choice == 1):
        c = maximumofnumbers(4, 5)
        print(str(c))
        continue
    elif(choice == 2):
        fizz_buzz(802)
        continue
    elif(choice == 3):
        speed_of_drivers(105)
        continue
    elif(choice == 4):
        show_numbers()
        continue
    else:
        print("invalid choice")
        break
