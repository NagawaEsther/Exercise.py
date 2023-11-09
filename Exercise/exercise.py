# Create a user class with properties i.e) name,age,location
#Create a new instance of the user class(a new object)
#Access the user's name and age
#Create a function for the user class that prints a users location
#print the users loctaion using this function

# Define the User class with properties
class User:
    def __init__(user, name, age, location):
        user.name = name
        user.age = age
        user.location = location

# Create a new instance of the User class
user = User("Esther", 22, "Kampala")

# Access the user's name and age
name=input("Enter your name:")
age=input("Enter your age:")
print(name)
print(age)

# Create a function for the User class that prints a user's location
def print_location(user):
        print("user's location:",user)

# Print the user's location using the print_location function
print_location("Kampala")
