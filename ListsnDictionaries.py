## exmaple of proper List syntax
best_languages = ["JavaScript", "Go", "Rust", "Python", "C"]

# Syntax of standard "Slicing": 
    my_list[ start : stop : step ]

# Syntax of Omitting "Step Slicng": 
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers[:3] # Gives [0, 1, 2]
    numbers[3:] # Gives [3, 4, 5, 6, 7, 8, 9]

# Syntax of Step selection
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers[::2] # Gives [0, 2, 4, 6, 8]

# Synatax of Reverse Slicing
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers[-3:] # Gives [7, 8, 9]

# List Deletion (Use Del) 
def trim_strongholds(strongholds):
    del strongholds[0] # Deletes the first item from the list
    del strongholds[-2:] # Deletes the last 2 items from the list


## length function that shows the highest list item record
def get_last_index(inventory):
    return len(inventory) - 1

## Replace indexed list item absed on whether it matches the trigger (this case if 'Inventory' list has 'Iron Ore' in the 2nd slot it will update Iron Ore to Iron Bar
def smelt_ore(inventory):
    if inventory[1] == 'Iron Ore':
        inventory[1] = 'Iron Bar'
    return inventory

## Adds id's based on the number
def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)
        i+=1

    return player_ids

## Removes the last item from the list every loop
    for i in range(0, len(inventory)):
        item = inventory.pop()

## Adds counter for each item in list, this can be used to show duplicates

    for i in range(0, len(items)):

        
        if items[i] == "Potion":
            potion_count += 1
        elif items[i] == "Bread":
            bread_count += 1
        elif items[i] == "Shortsword":
            shortsword_count += 1

## adds highest item on list to Max_so_far

def find_max(nums):
    max_so_far = float("-inf")
    pass

    for nums in nums:
        if nums >= max_so_far: 
            max_so_far = nums
    return max_so_far


## adds numbers from list to another list if they are odd. this uses the Modulo "%", can be re-written to return whether a number is odd or even.
    for i in range(0, num):
        if i % 2 == 1:
            odd_numbers.append(i)


## Concat lists
total = [1, 2, 3] + [4, 5, 6]
# OR 
combined_list = list_1 + list_2 + list_3


## List Operations - Contains
    return weapon in top_weapons #Returns True if "weapon" is within "top_weapons" (False if not True)
    return weapon not in top_weapons #Returns False  if "weapon" is within "top_weapons" (True if not False)
## Tuples (Static Lists within lists)
    heroes = [
        ("Glorfindel", 2093,True), #The Tuple is containted within round brackets within the square brackets
        ("Gandalf",1054,False),
        ("Gimli",389,False),
        ("Aragorn",87,False)
    ]
