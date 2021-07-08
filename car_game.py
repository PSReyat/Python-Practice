print("Available commands:\n1) help\n2) start\n3) stop\n4) quit\n")
command = input(">").lower()
started = False

while command != "quit":
    if command == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to exit the program\n")
    elif command == "start":
        if started:
            print("Car has already started.\n")
        else:
            started = True
            print("Car has started.\n")
    elif command == "stop":
        if started:
            started = False
            print("Car has stopped.\n")
        else:
            print("Car has already stopped.\n")
    else:
        print("Input not recognised. Please enter 'help' for list of valid inputs.\n")

    command = input(">").lower()

print("You have quit the program.")