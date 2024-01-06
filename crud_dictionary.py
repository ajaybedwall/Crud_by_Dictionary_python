

#  CRUD USING DICTIONARY


dict = {"name":"","number":"","gmail":"","password":""}

while True:
    print("\n 1. Create Data\n 2. Read Data\n 3. Update Data\n 4. Delete Data  ")
    user = int(input("Choose option: "))

    if user == 1:
        valu = input("Enter your name: ")
        dict["name"]=valu

        while True:
            number = input("Enter your value (10-digit number): ")

            if len(number) == 10 and number.isdigit():
                dict["number"] = number
                break
            else:
                print("Invalid mobile number. Please enter a 10-digit number.")
        while True:
            gmail = input("Enter your gmail address: ")
            if gmail.count('@') == 1 and '.' in gmail.split('@')[1] and gmail.endswith("com"):
                dict["gmail"] = gmail
                break
            else:
                print("Invalid gmail address. Please enter a valid gmail address.")
        while True:
            password=input("Enter your password: ")
            if len(password) >= 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
                dict["password"]=password
                break
            else:
                print("Invalid password. Please enter a valid password.")         
    elif user == 2 :
        all_empty = all(not value for value in dict.values())
        while True:
            if all_empty:
                print("  data in the dictionary are empty.")
                break
            check=input("Enter your password: ")
            if check == dict["password"]:
                print("Your data is:")
                print("Full Name:", dict["name"])
                print("Mobile Number:", dict["number"])
                print("Email Address:", dict["gmail"])
                print("Password:", dict["password"])
                break
            else:
                print("Incorrect password. Please set a password.")
    elif user == 3:
        all_empty = all(not value for value in dict.values())
        if all_empty:
            print("All data in the dictionary are empty !!!  Fill YOUR Data")
            continue
        print("Choose data to update:")
        print("1. Name\n2. Number\n3. Gmail\n4. Password")
        user = int(input("Enter your choice: "))
        if user == 1:
            new_data = input(f"Enter your new {dict['name']}: ")
            dict["name"]=new_data
            print(f" your new name is :-{dict['name']}: ")
        elif user == 2:
            new_data = input(f"Enter your new {dict['number']}: ")
            dict["number"]=new_data
            print(f" your new number is :-{dict['number']}: ")
        elif user == 3:
            new_data = input(f"Enter your new {dict['gmail']}: ")
            dict["gmail"]=new_data
            print(f" your new gmail is :-{dict['gmail']}: ")
        elif user == 4:
            new_data = input(f"Enter your new {dict['password']}: ")
            dict["password"]=new_data
            print(f" your new password is :-{dict['password']}: ")
        else:
            print("Invalid choice. Please enter a valid number.")
    elif user == 4:
        all_empty = all(not value for value in dict.values())
        if all_empty:
            print(" creat your account ")
            continue
        print("what do  you want to delete")
        print("1. Name\n2. Number\n3. Gmail\n4. Password")
        user = int(input("Enter your choice: "))
        if user ==1:
            del dict["name"]
            print("your name is deleted")
            print(dict.keys())
        elif user==2:
            del dict["number"]
            print("your number is deleted")
            print(dict.keys())
        elif user==3:
            del dict["gmail"]
            print("your email address is deleted")
            print(dict.keys())
        elif user==4:
            del dict["password"]
            print("your password is deleted")
            print(dict.keys())
        else:
            print("Invalid choice. Please enter a valid number.")
            continue
    else:
        print("Invalid choice. Please enter a valid number.")










