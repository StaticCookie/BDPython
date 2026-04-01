## exmaple of proper List syntax
best_languages = ["JavaScript", "Go", "Rust", "Python", "C"]

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
        # ?
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
