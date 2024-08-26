# firsr assignment create a list of dictionaries
def list_to_dict(player):
    # Define the keys for the dictionary  (Number, Position, Name, Date of Birth, Caps, Club, Country, Club, Club Country, Year)
    Keys = ["Number" , "Position" , "Name" , "Date of Birth" , "Caps" , "Club" , "Country" , "Club" , "Club Country" , "Year" ]
    # Initialize an empty list to store the dictionaries.  (result)  (will hold the final list of dictionaries) 
    result = []
    # Iterate over the list of lists (player) and create a dictionary for each player with the defined keys and values.
    for players in player:
        # Use the zip function to pair up the keys and values from the players list.
        playerdict = dict(zip(Keys, players))
        result.append(playerdict)
    return result


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
print(list_to_dict(SQUADS_DATA))