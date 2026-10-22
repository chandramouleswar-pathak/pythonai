
player={
    "name":"black devil",
    "health":400,
    "location":"cryo_lab"
}
ship_map={
    "cryo_lab":{
        "north":"Main corridor"
    },
    "Main corridor":{
        "south":"cryo_lab"
    },
}
active=True
while active:
    print(f"\n Cureent location is : {player["location"]}")
    command=input("where to? (or type quit)")
    if command=="quit":
     active=False
     print("the game is closing!")
    elif command=="north" or command=="south":
     current=player["location"]
     next_room=ship_map[current][command]
     player["location"]=next_room
     print(f"you walked to the  {next_room}")