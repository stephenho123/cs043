from database import Simpledb
db = Simpledb("data.txt")
file = open("data.txt", "w")
file.close()
while False == False:
    print("ENTER COMMAND(a, f, d, u, or q)!!!")
    command = input()
    if command == "a":
        print("Enter name")
        name = input()
        print("Enter phone number")
        number = input()
        db.add(name,number)
    elif command == "f":
        print("Enter name")
        name = input()
        db.find(name)
    elif command == "d":
        print("Enter name")
        name = input()
        db.delete(name)
    elif command == "u":
        print("Enter name")
        name = input()
        names = db.find(name)
        if names != None:
            print("Enter phone number")
            number = input()
            db.update(name,number)
    elif command == "q":
        break
