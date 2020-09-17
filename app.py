start = False
stop = False

while True:
    command = input("commands: 'start' , 'stop '  >").lower()
    if command == "start":
        if start == False:
            start = True
            stop = False
            print("car started")
        else:
            print("you cant start,car already started")
    elif command == "stop":
        if stop == False:
            stop = True
            start = False
            print("car stopped")
        else:
            print("you cant stop,car already stoppped")


print("Hello world")



# This is just message from local machine to remote repo
# I think i have done many things with git
