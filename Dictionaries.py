#----------------------------------------------------------------------------#
# simple dicationary decleration & return
#----------------------------------------------------------------------------#

def get_character_record(name, server, level, rank):
    
    account_information = {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": name + "#" + server
    }

    return account_information 

#----------------------------------------------------------------------------#
# dicationary process that counts duplicate values and returns the count
#----------------------------------------------------------------------------#
def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        
        if enemy_name not in enemies_dict:
            enemies_dict[enemy_name] = 1
        else: 
            enemies_dict[enemy_name] += 1
    return enemies_dict
#----------------------------------------------------------------------------#
# dicationary process that returns the highest score
#----------------------------------------------------------------------------#
def get_top_scorer(scores):
    top_name = None
    top_score = None

    for name in scores:
        score = scores[name]
        if top_score is None or score > top_score:
            top_name = name
            top_score = score

    return top_name

#----------------------------------------------------------------------------#
# dicationary process that returns the lowest distance & includes clause for no inputs.
#----------------------------------------------------------------------------#
def get_most_common_enemy(enemies_dict):
    
    lowest_distance = None

    if len(enemies_dict) == 0:
        return lowest_distance

    else:
        for name in enemies_dict:
            distance = enemies_dict[name]
            if lowest_distance is None or distance > lowest_distance:
                closest_enemy = name
                lowest_distance = distance

    return closest_enemy
    
#----------------------------------------------------------------------------#
# dicationary updates count per item in dictionary, if its not already in inventory it adds 1 to inventory
#----------------------------------------------------------------------------#
def build_gem_inventory(picked_up):
    inventory = {}
    for gem in picked_up:
        if gem in inventory:
            inventory[gem] += 1
        else:
            inventory[gem] = 1
    return inventory
