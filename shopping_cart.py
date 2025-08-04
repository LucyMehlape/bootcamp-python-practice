
#Create a shopping cart program that will continuously the user for a food product and the price of that product.
#Have an exit clause if the user wishes to stop adding more items to their cart.
#At the end show the user all the items in their cart and the total price of all items.

foods = []
prices = []
total_price = 0.0

while True:
    food = input("Enter a food product or press q to quit: ")
    if food.lower()=='q':
        break
    else:
        price = float(input(f"Enter the price of {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("-----YOUR CART-----")   

for food in foods:
    print(food, end=", ")     
    
for price in prices:
    total_price += price
 
print("\n")   
print(f"Your total price is: R{total_price}")
        