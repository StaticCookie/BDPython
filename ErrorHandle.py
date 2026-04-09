## Error documentation for Py: https://docs.python.org/3/library/exceptions.html

#----------------------------------------------------------------------------#
# Calls function and checks for varios errors 
  # Index Error returns: Index is too high
  # custom error for negative integers
  # Catch all error
#----------------------------------------------------------------------------#
def process_player_record(player_id):
    try:
        get_player_record(player_id)
        return get_player_record(player_id)
    except IndexError: # Index Error returns: Index is too high
        return "index is too high"
    except Exception as e: # Catch all error
            return str(e) 

def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed") # custom error for negative integers
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]
#----------------------------------------------------------------------------#
# Raises error handling when 1 variable that is expected to be larger is not.
# Otherwise if no error, function returns the difference.
#----------------------------------------------------------------------------#

def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception("not enough gold")
    return gold_available - price
