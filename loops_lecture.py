# GET LOOPY

# looping through a list of ice cream flavors
#             0            1            2          3             4               5
flavors = ["vanilla", "chocolate", "blueberry", "coffee", "chocolate chip", "pistachio"]
# for keyword iterator variable in keyword thing we're iterating through
for flavor in flavors:
    print(flavor)

for flavor in flavors:
    print(f"Oh boy do i sure love sampling {flavor} ice cream")

# using the range function to loop
# range(start, stop, step)
print(range(6))
for i in range(6):
    print(i)

# looping by index using range
#             0            1            2          3             4               5
flavors = ["vanilla", "chocolate", "blueberry", "coffee", "chocolate chip", "pistachio"]
for i in range(6): # 6 being the length of our flavors list
    print(flavors[i]) # flavors[0] flavors[1] falvors[2]...

# using range(len(list)) to get the indexes for a specific list with an unknown length
for i in range(len(flavors)):
    print(i, flavors[i])

x, y = 1, 2 

# looping with enumerate(our_list)
for i, flavor in enumerate(flavors):
    print(i, flavor) # [(0, "vanilla"), (1, "chocolate")...]

# ============= DOUBLE FOR LOOPS for the DOUBLE SCOOP ===================
#             0            1            2          3             4               5
flavors = ["vanilla", "chocolate", "blueberry", "coffee", "chocolate chip", "blueberry", "pistachio"]
toppings = ["sprinkles", "chocolate syrup", "whipped cream", "cherry"]
for flavor in flavors:
    for topping in toppings:
        print(f"Lets try a scoop of {flavor} with some {topping} on top")

# break stops loops from running
for flavor in flavors:
    print(flavor)
    if flavor == "chocolate":        
        print("Oh yummy! Thats my favorite! No need to keep looking for ice cream")
        break


# continue to skip over an iteration
for flavor in flavors:
    if flavor == "blueberry":                    
        continue #skip over blueberry
        
    print(flavor)
print(flavors)

# pass creates a placeholder until we figure out what to do with that code block
flavors = ["vanilla", "chocolate", "blueberry", "coffee", "chocolate chip", "blueberry", "pistachio"]
for flavor in flavors:
    if flavor == "coffee":
        pass # ill figure this out later
    print(flavor)


# Looping through multiple lists of the same length by index
#                 0       1        2         3
booth_types = ["Food", "Games", "Music", "Crafts"]
#                    0           1        2         3
schedule_times = ["10:00 AM", "1:00 PM", "3:00 PM", "5:00 PM"]
#                 0          1              2           3
items_needed = ["Grill", "Tickets", "Instruments", "Paint"]

for i in range(len(booth_types)):
    booth = booth_types[i]
    time = schedule_times[i]
    item = items_needed[i]
    print(f"{booth} Booth - Schedule: {time}, Item Needed: {item}")

#               0           1           2
flavors = ["chocolate", "vanilla", "strawberry"]
#             0             1             2
toppings = ["sprinkles", "cherry", "chocolate syrup"] 

for i in range(len(flavors)):
    print(i)
    ice_cream = flavors[i]
    topping = toppings[i]
    print(f"On my {ice_cream} ice cream i like {topping}")

# .count() and sum()
# how to do both with for loop
item_prices = [2.99, 5.49, 3.25, 13.99, 4.75]
# using sum to calculate the total price
print((sum(item_prices)/len(item_prices))) # average item price

# getting a sum with a for loop
item_total = 0 # counter variable, but we're continuously add to this for each item in our item_prices
for price in item_prices:
    item_total += price
print(f"Thank your for shopping at Aldi! Your total is {item_total}")
print(item_total/len(item_prices))

# working with lists in lists with loops
inventory = [
    ["Apples", 5],
    ["Bananas", 2],
    ["Oranges", 0],
    ["Milk", 1],
    ["Eggs", 12]
]

print(inventory[1][1])
reorder_threshold = 3


# check each item (which is a list with two items) and see what needs to be reordered
for item in inventory:
    name, quantity = item #["item", integer quantity]
    if quantity < reorder_threshold:
        print(f"{name} needs to be reordered")
    else:
        print(f"We have a lot of {name} in stock")


# ===================== WONDERFUL WORLD OF WHILE LOOPS =============================
# syntax for while loop
# while condition_is_true:
    # do somethign here until that conidtion is no longer true

# variable that we're checking is less than 5
marshmallows = 0
# setting the condition for the while loop to run
while marshmallows < 5:
# we add 1 to marshmallows variable for each iteration
    marshmallows += 1
    print(marshmallows)
    # eventually marshmallows increments over 5 and the while loop breaks
    

# be careful with our conditions
# if our condition is never true our while loop will never run
marshmallows = 0
# setting the condition for the while loop to run
while marshmallows > 5: # wont run because it will never be true with the current variable
# we add 1 to marshmallows variable for each iteration
    marshmallows += 1
    print(marshmallows)
    # eventually marshmallows increments over 5 and the while loop breaks

# being careful that our condition is always true


# marshmallows = 0
# while marshmallows < 5: 
#     marshmallows -= 1
#     print(marshmallows)

# in the above the while loop will never stop running
# because we're decrementing our counter and it will never be greater than 5

# using user input with a while loop
# break when the user says quit
# while True:
#     user_input = input("Say 'stop' to end the refill")
#     if user_input.lower() == 'stop': #.lower() is a string method that changes all characters to lower case
#         print("Enjoy your coffee")
#         break
#     else:
#         print("Heres more coffee")


# adding items to a shopping cart
# cart = []
# print("Hi welcome to Aldi, what can i help you with today?")
# while True:
#     user_input = input("Tell us what you'd like to add to your cart or say 'quit' to quit: ")
#     if user_input == "quit":
#         print("Thanks for shopping here are your items: ")
#         for item in cart:
#             print(item)
#         break
#     else:
#         cart.append(user_input)
#         print(f"Your cart so far {cart}")



# to do list
# to_do_list = []

# def add_item(to_do_list):
#     item = input("What do you need to do? ")
#     to_do_list.append(item)
# while True:
#     choice = input("What would you like to do? add/remove/view/mark as complete")
#     if choice == "add":
#         add_item()
#     elif choice == "remove":
#         remove_item()

import random
names = ["Kayla", "Victor", "Chris", "Karen", "Winter"]
# random.choice() gives us a random item from an iterable
print(random.choice(names))

# randint gives a random number from a range of numbers
# roll some dice
for num in range(10):
    print(num)
    dice_roll = random.randint(1,20) #includes both the 1 and the 20
    print(f"You rolled a {dice_roll}!")

# random.shuffle shuffle a list of stuff
playlist = ["N95", "Careless Whipser", "21 Gun Salute", "Whats Up"]
random.shuffle(playlist)
for song in playlist:
    print(song)

# random.choice with a while loop
snacks = ["peanut butter cups", "fruit snacks", "carrot stick", "chocolate bar"]
# picked_snack = ''
while picked_snack != 'chocolate bar':
    picked_snack = random.choice(snacks)
    print(f"You got a {picked_snack}")
    if picked_snack != "chocolate bar":
        print("lets pick again!")
    else:
        print("Yay chocolate")


# while True:
#     picked_snack = random.choice(snacks)
#     print(f"You got a {picked_snack}")
#     break
#     if picked_snack != "chocolate bar":
#         print("lets pick again!")
#     else:
#         print("Yay chocolate")
#         break



