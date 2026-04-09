 for i in range(len(items),0,-1):
#i = Incriment
#range = range(start, stop, step)

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

## loop that adds 5 XP per level & keeps tally per level gained
def calculate_experience_points(level):
    counter = 0
    xp_so_far = 0
    xp_next_level = 0
    
    while level > counter:
        counter += 1
        
        xp_so_far += xp_next_level
        xp_next_level = counter * 5

    return xp_so_far

## Rotate player list
def rotate_turn_order(players):

    player_len = len(players) # only required for checking if input players are blank / empty.
    new_order = players


    if player_len != 0: #checks if there is a list
        rotated_player = players[0]
        new_order.pop(0)
        new_order.append(rotated_player)
    else:
        new_order = [] # returns null if no input
        
    return new_order


#### Only returns integers
def remove_nonints(nums):
    updated_list = []
    for i in nums:
        if type(i) == int:
            updated_list.append(i)
        if type(i) == str: 
            continue
        if type(i) == float:
            continue
    return updated_list

    
    
