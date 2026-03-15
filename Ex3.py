def track_names():
    names = set()
    while True:
        name = input("Type a name here: ")
        if name == "":
            break
        if name in names:
            print("This name is exists already, type new name.")
        else:
            print("This name has been saved.")
            names.add(name)
    print("This is the list of names that you have entered:")
    for n in names:
        print(n)
track_names()