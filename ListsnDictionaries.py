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
