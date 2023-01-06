# Author: Raed LNU
# Date: 26 October 2022
# This file generates the receipt
#
#A constant that holds the tax rate.
TAX = 0.13

#A function that stores the pizza size and the cost of extra toppings corresponding to that specific size.
def extraTopping(size) :
    toppingsPrice = {"S": 0.50, "M": 0.75, "L": 1.00, "XL": 1.25}
    return toppingsPrice.get(size)

#The main generateReceipt function that takes in the parameter PizzaOrder
def generateReceipt(pizzaOrder) :
    #If the user did not order anything, it prints "you did not order anything"    
    if pizzaOrder == []:
        print("You did not order anything")
        # Returns true if the argument is a string.
        
    #If the user orders something then it executes the following code
    else:
        #Initialize the variables
        totalPrice = 0.0
        text = "Your order: \n"
        numPizzas = 1
        toppings = 0
        #For every element in the PizzaOrder list, it gets the size.
        for i in pizzaOrder:
                size = i[0]
                #If the size is "S", "M", "L" or "XL" then it sets the corresponding price to that size
                if size == "S":
                    price = 7.99
                    #Gets the toppings for that pizza, which is in the 2nd element of the list.
                    toppings = i[1]
                    #Price gets added to totalPrice
                    totalPrice += price
                    #Varible "text" stores the str with the proper formatting.
                    text += f"Pizza {numPizzas}: {size}                  {price}\n"
                elif size == "M" :
                    price = 9.99
                    toppings = i[1]
                    totalPrice += price
                    text += f"Pizza {numPizzas}: {size}                  {price}\n"
                elif size == "L" :
                    price = 11.99
                    toppings = i[1]
                    totalPrice += price
                    text += f"Pizza {numPizzas}: {size}                  {price}\n"
                elif size == "XL" :
                    price = 13.99
                    toppings = i[1]
                    totalPrice += price
                    text += f"Pizza {numPizzas}: {size}                  {price}\n"
                    
                #for every topping in the order, the string is formatted so that the toppings are all uppercase, start in a new line and have a "-" behind them.
                for topping in toppings :
                    text += f"- {topping.upper()}\n"

                #If there are more than 3 toppings then the toppingfee gets assigned according to the size of the pizza.
                if len(toppings) > 3 :
                    toppingFee = extraTopping(size)
                
                
                # Returns a textual representation of the total price of all the toppings & also adds 1 to numPizzas everytime a pizza is ordered.
                for Z in range (len(toppings) - 3) :
                    totalPrice = totalPrice + toppingFee
                    text += f"Extra Topping ({size})      {toppingFee:.2f}      \n"
                numPizzas += 1
        
        # Calculate the tax.
        tax = totalPrice * 0.13
        
        # prints a textual representation of the tax & the total price including tax.
        text += f"Tax:                        {(tax):.2f}\n"
        text += f"Total:                      {(totalPrice + tax):.2f}"
        print (text)


