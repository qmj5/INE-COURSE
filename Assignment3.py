def group_dict2(players):
    keys = ["Number" , "Position" , "Name" , "Date of Birth" , "Caps" , "Club" , "Country" , "Club" , "Club Country" , "Year" ]
    # initialize dictionary 
    group_by_dict = {}
    # iterate over players and create dictionary with keys and values  and add it to group_by_dict dictionary 
    # with country as key and position as nested key 
    # and append player info to the list  for that position in the result dictionary.  
    # finally, return the result dictionary.  (group_by_dict) 
    for player in players:
        player_dict = dict(zip(keys, player))
        postion = player_dict["Position"]
        country = player_dict["Country"]
        if country not in group_by_dict:
            # the value for that country if is not in group_by_dict initialize it as empty dictionary
            group_by_dict[country] = {}
        if postion not in group_by_dict:
            # the value for that postion if is not in group_by_dict initialize it as empty list
            group_by_dict[country][postion] = []
        group_by_dict[country][postion].append(player)
    return group_by_dict



# Test the function with provided data
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

# Test the function
print(group_dict2(SQUADS_DATA))


