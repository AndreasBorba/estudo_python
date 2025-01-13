requested_toppings = ['mushrooms']
if requested_toppings != 'anchovies':
    print("Hold the anchovies!")
# The output is:
# Hold the anchovies!

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' not in requested_toppings:
    requested_toppings.append('mushrooms')
    print("Adding mushrooms.")
if 'pepperoni' not in requested_toppings:
    requested_toppings.append('pepperoni')
    print("\nAdding pepperoni.")
if 'extra cheese' not in requested_toppings:
    requested_toppings.append('extra cheese')
    print("Adding extra cheese.")
print("\nYour pizza has:")
for requested_topping in requested_toppings:
    print(requested_topping)

print("\nFinished making your pizza!")

requested_toppings.insert(1, 'anchovies')
print(requested_toppings)