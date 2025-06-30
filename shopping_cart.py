# create a shopping cart programme that will continously ask the user for food product and the price of that product
# have exit clause if the user wishes to stop adding more things to their cart
# at the end show the food items and the total cost to the user

foods = []
prices = []
total = 0

while true:
      food = input ("enter a food to buy or press q to quit;")
      if food.lower() == "q":
         break 
      else:
         price = float(inpit (f"enter the price of the{food}:R"))
         foods.append(food)
         price.append(price)

print ("----- YOUR CARR -----")

for food in foods:
     print (food)
     
for price in prices:
     total += price

prnit("your total is: R{total}")

         
         