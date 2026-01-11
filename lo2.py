granted = False

def grant():
    global granted
    granted = True

def login(name, password):
    success = False  
   
    file= open("lo.txt", "r") 
    for line in file:
        a, b = line.split(",")  
        b = b.strip()  
        if a == name and b == password:
            success = True
            break
    
    
    if success:
        print("Login successful")
        grant
    else:
        print("Wrong username or password")

def register(name, password):
    with open("lo.txt", "a") as file:
        file.write(f"{name},{password}\n")  

def access(option):
    if option == "login":
        name = input("Enter your name: ")
        password = input("Enter password: ")
        login( name, password)
    else:  
        print("Enter your name and password to register:")
        name = input("Enter your name: ")
        password = input("Enter password: ")
        register( name, password)

def begin():
    global option
    print("Welcome to the library dashboard!")
    option = input("Login or Register (login, reg): ").lower()
    
    if option not in ["login", "reg"]:
        print("Invalid option. Please choose 'login' or 'reg'.")
        begin()  

begin()
access(option)
if granted:
    print("Welcome to the library!")
else:
    print("Please try again.")