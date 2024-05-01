# Python Lists
# Ordered Collection of items, where each item has a specific place, known as an index

# declaring list variables
# empty list
empty_list = [] #square brackets is always a list

# a list with stuff in it
# each item in a list needs to be separated by a comma
potions = ["Healing", "Invisiblity", "Strength"]

print(potions)

# positions in a list - index
# index 0 is always the first position
# -1 this is always the last position, regardless of list length
#             0            1              2 or -1
potions = ["Healing", "Invisiblity", "Strength"]

# accessing items in a list by index
# list_variable[index_number] - index will always be an integer
# access the first position of my potions list
print(potions[0]) # "Healing"

my_potion = potions[1]

print(my_potion)

# accessing the last item in our list
# with the index number itself or -1
print(potions[2])
print(potions[-1])

# Lists maintain the order we set
colors = ["red", "blue", "green", "yellow"]
print(colors)

# Python's dynamic typing
my_variable = "string"
my_variable = 5
# variables arent locked to a specific type upon declaration

# Python lists are hella flexible
#             0      1     2          3
weird_list = [12, "Duck", 5.46, ["Bob", "Linda"]]
print(weird_list)
print(weird_list[3][1])
print(weird_list[-1])
print(weird_list[-1][-1])


# How do we add and remove things to our list
# .append()
# our_list.append(thing we're appending)
golf_supplies = ["Golf Cart", "Golf Balls", "Golf Clubs"]
golf_supplies.append("Ball Polisher")
print(golf_supplies)
golf_supplies.append("Vizor")
golf_supplies.append("Caddy")
print(golf_supplies)

# removing from a list in python
# ourlist.remove(thing we're removing)
# ourlist.pop() #removes by index and if no argument is provided, it pops the last index
# pop also returns the value that is popped
# del our_list[postion]
# our_list.clear() clears out the list 


golf_supplies.remove("Ball Polisher") # returns None
print(golf_supplies)
# golf_supplies.remove() TypeError because remove takes exactly 1 argument and weve given 0

popped_item = golf_supplies.pop() #no argument so its going to default to -1 -> last index
print(popped_item)
# returns the item that was popped
print(golf_supplies)
# popping an item with an index
print(golf_supplies.pop(1))
print(golf_supplies)

# del which just wipes whatever it is we're delling
# be careful with del because it is quite unforgiving
adventuring_supplies = ["Sword", "Canteen", "Potions", "Cape", "Rope", "Alternator", "Fruit Snacks"]
print(adventuring_supplies)
del adventuring_supplies[1]
print(adventuring_supplies)
# del adventuring_supplies
# print(adventuring_supplies)

adventuring_supplies.clear()
print(adventuring_supplies)

# Lists with duplicate items
flowers = ["rose", "lily", "rose", "daisy", "lily", "rose", "its been 84 years"]
# our_list.count(the thing we're counting)
print(flowers.count("rose"))

lilies = flowers.count("lily")
print(lilies)
flowers.remove("rose") # this removes only the first occurence
print(flowers)

more_flowers = ["rose", "lily","rose", "rose", "daisy", "lily", "rose", "its been 84 years"]
# trying to remove with a for loop
for flower in more_flowers:
    if flower == "rose":
        more_flowers.remove(flower)
print(more_flowers)

while "rose" in more_flowers:
    more_flowers.remove("rose")
print(more_flowers)

# adding to a list by postion
# our_list.insert(postion, thing we're inserting)
hobbies = ["video games", "kayaking", "golfing", "drankin"]
hobbies.insert(2, "hiking")
print(hobbies)
hobbies.insert(3, "reading")
print(hobbies)
hobbies.insert(1, "basketball")
print(hobbies)

# ====================== SORTING LISTS ==========================
# our_list.sort() -> alter our original list and sort it - in place
# sorted(our_list) -> copies our list and sorts the copy - out of place
numbers = [5, 1, 6, 100, 13, 2, 4, 17, 12]
print("numbers before .sort", numbers)
numbers.sort()
print("numbers after .sort", numbers)

# reverse sorting a list
even_more_numbers = [5, 1, 6, 100, 13, 2, 4, 17, 12]
even_more_numbers.sort(reverse=True)
print(even_more_numbers)

more_numbers = [5, 1, 6, 100, 13, 2, 4, 17, 12]
sorted_numbers = sorted(more_numbers) #reverse=True can go in the parentheses as an additional argument
print(more_numbers, "unchanged")
print(sorted_numbers, "copy is sorted")

# len() -> length or how many items are inside our list
names = ["Chris", "Farzin", "Victor", "Winter", "Karen", "andy"]
print(len(names))

names.sort()
print(names)
# our_list.reverse()
# names.reverse()
# print(names)

# Checking if two variables are pointing to the same list object
guest_1 = [1, 2, 3]
guest_2 = guest_1
guest_3 = [1, 2, 3]

print(guest_1 is guest_2)
print(guest_1 is guest_3)
print(guest_1 == guest_3)

# Membership check in a list using in
guest_list = ["Alice", "Bob", "Charlie"]
print("Alice" in guest_list) # True
print("Dana" in guest_list) # False

if "Bob" in guest_list:
    print("awww shooot, who invited Bob?")
else:
    print("Oh thank god, no Bob!")

print("Bob" not in guest_list) # False

guestlist_a = ["Alice", "Bob", "Charlie"]

guestlist_b = ["Alice", "Charlie", "Stephen"]

if guestlist_a[1] in guestlist_b:
    print("We should definitely invite ", guestlist_a[0])
else:
    print("maybe we wont invite them")

# Deeper Dive of len()
hobbies = ["video games", "golfing", "hiking", "basketball", "reading"]
print(len(hobbies)) # number of items in my list
# 0 1 2 3
print(hobbies[len(hobbies) - 1]) #accessing the last item in our list using len(list) - 1
#                4        - 1  =  3
last_index = len(hobbies) - 1 # 3
print(hobbies[last_index]) #hobbies[3] or hobbies[-1]

# setting other postions to variables
# use those variables to index into the list
position = 2
favorite_hobby = hobbies[position]
print(favorite_hobby)

# using the floor operator to grab the middle index of our list
middle_index = len(hobbies) // 2
print(len(hobbies))
print(len(hobbies)/2)
print(middle_index)
print(hobbies[middle_index])




# Concatenation or Combingin lists
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "peas"]

weird_salad = fruits + vegetables # combines fruits list with vegetables list
print(weird_salad)


# list.copy()
salad_clone = weird_salad.copy()
print(salad_clone)

# list.extend()
vegetables.extend(fruits)
print(vegetables)

# " ".join(our_list) -> joins the elements of a list together based on a joiner
story_time = ["once", "upon", "a", "time", "there", "lived", "an", "ogre"]
our_story = " ".join(story_time)
print(our_story.capitalize()) #capitalize() captialzies the first letter of our string


# ============= LIST SLICING =============
# allows us to grab specifc chunks or slices of our list
#           included     not included
#             0 default   last index    1
# our_list[start index:stop index:step index]
#              0            1        2          3         4              5       6          7            8
hobbies = ["video games", "golf", "hiking", "reading", "basketball", "anime", "chess", "opal mining", "soccer"]
print(hobbies[2:]) #slice from index 2 to the rest of my list
# creating a new list variable with a slice
fav_hobbies = hobbies[3:6] # slices starting at reading and stops right before index 6 - anime
print(fav_hobbies)
step_by_two = hobbies[::2]
print(step_by_two)
# reversing a list with slicing
reversed_hobbies = hobbies[::-1]
print(reversed_hobbies)
# start from the beginning and stop at index 5
print(hobbies[:5])


# what happens if we try to access an index that doesn't exist in the list
print(hobbies[9]) # IndexError because 9 is not a position in our hobbies list








