command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car is stopped")
    elif command == "help":
        print("""Start - To start the car
Stop - To stop the car
Quit - To quit
              """)
    elif command == "quit":
        break
    else:
        print("I can't understand you")/Users/pyt/PycharmProjects/LearningPython