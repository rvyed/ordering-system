# Author: Raed LNU
# Date: 26 October 2022
# This file is the heart of the program that sends the pizza order to the receipt

#Imports everything from the file pizzaReceipt.py
from pizzaReceipt import*

# A tuple that contains the 15 toppings
TOPPINGS = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")

# stores the pizza order.
pizzaOrder = []  
 
# Function to add a Pizza.
def addPizza():

    # Size of the pizza.
    size = ''
    # Sets the storeToppings to the given list.
    storeTopping = []

    # Sets the topping of a string.
    topping = ''

    # Asks for user input for size and converts it to upper case, if the size is not S,M,L,XL then it will repeat the same statement.
    while size != "S" and size != "M" and size != "L" and size != "XL":
        size = (input("Choose a size: S, M, L, or XL: ")).upper()

    # While the topping is not "X" because X is used to stop the list at anytime. Asks the user to input the toppings.
    while topping != 'X':
        topping = (input('Type in one of our toppings to add it to your pizza. To see the list of toppings, enter "LIST". When you are done adding toppings, enter "X"\n')).upper()

        # Add a new topping to your pizza, if the topping is in the tuple then it is accepted.
        if topping in TOPPINGS:
            storeTopping.append(topping)
            print("Added", topping.upper(), "to your pizza")
        # Prints the list of the toppings    
        elif topping == 'LIST':
            print(TOPPINGS)
        # Breaks the code, if the letter "x" is typed.
        elif topping == "X":
            break
        # If a topping that is not in the tuple and is not "x" nor "list", returns "Invalid topping"
        else:
            print("Invalid topping")

    #A tuple that stores the size and the toppings with the correct format.
    PizzaTuple = (size, storeTopping)
    #the order is appeneded to the PizzaTuple 
    pizzaOrder.append(PizzaTuple)

    # Asks the user if they want to continue ordering.
    Continue = input("Do you want to continue ordering?: ").upper()
    # If the user does not type NO or Q then the function addPizza() is ran again which means another order is being added
    if Continue != "NO" and Continue != "Q":
        addPizza()
    # Otherwise it returns with the current order.
    else:
        return

#Asks the user if they want to order a pizza
PizzaTime = input("Do you want to order a pizza?: ").upper()
#If the user input is not "No" or "Q" then the function addPizza() is ran to create an order and the receipt is generated
if PizzaTime != "NO" and PizzaTime != "Q":
    addPizza()
    generateReceipt(pizzaOrder)
else:
    print("You did not order anything\n")
#If they dont want a pizza, it sets the pizzaOrder to a blank var.
    pizzaOrder = ''
    



    


