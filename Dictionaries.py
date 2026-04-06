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

