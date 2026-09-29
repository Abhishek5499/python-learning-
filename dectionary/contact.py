contacts = {}

name = input("Name:")
phone = input("phone:")
email = input("email:")
contacts[name]= {
    "phone":phone,
    "email":email
}

for name, details in contacts.items():
    print("Name:",name,
          "|phone:",details["phone"],
          "|email:",details["email"])