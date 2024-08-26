#Assignment 2 
def group_dict(player):
    Keys = ["Number" , "Position" , "Name" , "Date of Birth" , "Caps" , "Club" , "Country" , "Club" , "Club Country" , "Year" ]
    # create a new dictionary to hold the postion information for the player
    group_by_dict = {}
    # "" iterate over each player's information in the given list and add it to the result dictionary, grouping them by their position.  
    # If a position is not already in the result dictionary, add it with an empty list as its value.  
    # Then, append the player's information to the list for that position.  
    # Finally, return the result dictionary.
    for player_info in player:
        player_dict = dict(zip(Keys,player_info))
        postion = player_dict["Position"]
        if postion not in group_by_dict:
            group_by_dict[postion] = []
        group_by_dict[postion].append(player_info)
    return group_by_dict






SQUADS_DATA = [
  [
    "1",                                     # Number
    "GK",                                    # Position
    "Juan Botasso",                          # Name
    "(1908-10-23)23 October 1908 (aged 21)", # Date of Birth
    "",                                      # Caps
    "Quilmes",                               # Club
    "Argentina",                             # Country (Players Country)
    "Argentina",                             # Club Country
    "1930"                                   # Year
  ],
  [
    "9",
    "FW",
    "Roberto Cherro",
    "(1907-02-23)23 February 1907 (aged 23)",
    "",
    "Boca Juniors",
    "Argentina",
    "Argentina",
    "1930"
  ]
  # More Players...
]

print(group_dict(SQUADS_DATA))

