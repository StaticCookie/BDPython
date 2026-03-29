## Counts by 1 to 99
def print_numbers():
    for i in range (0,100):
        print(i)

## Counts by 1 from 5
def print_numbers_from_five_to(end):
    for i in range(5, end):
        print(i)

## Counts down by 1
def count_down(start, end):
    for i in range(start, end, -1):
        print(i)

## Loops number by summing them Numbers
def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total

## Loop that counts odd numbers
def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total

## While loop that runs 'While' 2 conditions exist (seperated by 'and')
def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance > 3:
        current_health += 1
        enemy_distance -= 2
    return current_health


## Loop that uses "continue" arugments which is used to prevent processing un-necessary steps.
def award_enchantments(start, end, step):
    counter = 0
    for quest_number in range(start, end, step):
        enchantment_strength = quest_number * 5
        counter += 1
        
        if counter < 3: 
            continue
        
        elif counter == 3:
            counter = 0 
            print(
            f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
        )
