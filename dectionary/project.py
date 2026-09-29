contacts = {
    "abhi" : 9035535499 , 'akash':9011, "vijay":959096
    }

while True:
    print("\n1.Add  2.View  3.Search  4.Delete  5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print(contacts)

    elif choice == "2":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "3":
        name = input("Search name: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("Not found")

    elif choice == "4":
        name = input("Delete name: ")
        if name in contacts:
            contacts.pop(name)

    elif choice == "5":
        break