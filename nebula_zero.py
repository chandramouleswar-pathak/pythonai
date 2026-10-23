player={
    "name":"black devil",
    "health":400,
    "location":"cryo_lab",
    "inventory":[]
}
ship_map={
    "cryo_lab":{
        "desc":"Rows of frost-covered stasis pods hum softly. Sparks fizz frm a cracked terminal.",
        "exits":{"north":"Main corridor"},
        "items":["plasma_tourch","hand granade",]
    },
    "Main corridor":{
      "desc":"A wide, metal hallway with flashing red emergency lights. Bulkhead doors leads in all directions.",
        "exits":{"south":"cryo_lab",
        "north":"command_bridge",
        "east":"Armory",
        "west":"Medbay"},
        "items":[]
    },
    "command_bridge":{
      "desc":"The ships nervr center. The mainview port looks out into thr dark void of nebula.",
      "exits":{"south":"Main corridor"},
      "items":["medkit"]
      },
      "Armory":{
        "desc":"Reinforced wepon lockers line the wall, most pried opened and looted.",
        "exits":{"west":"Main corridor"},
        "items":["security_keycard"]
      },
      "Medbay":{
        "desc":"Sanitized white tiles covered in shattered glass. Autodocs stand powered down",
        "exits":{"east":"Main corridor"},
        "items":["datapad"]
      }

}
active=True
print("===NEBULA ZERO BOOTED UP , SHIPS CONDITION IS NOT GOOD PLEASE SAVE IT HERO.===")
while active:
    current_room=player["location"]
    room_data=ship_map[current_room]
    print(f"\n Cureent location is : {player["location"]}")
    print(room_data["desc"])
    if room_data["items"]:
     print(f"\nITEMS FOUND INTHEE ROOM ARE:{'->'.join(room_data["items"])}")
    else:
      print("NO ITEMS ARE TO BE SEEN IT THE ROOM!SHIT.")
    available_exits=list(room_data["exits"].keys())
    print(f"EXITS AVAILABLE: {', '.join(available_exits)}")
    command= input("\nAction !!move,Take <item>,Inventory,quit!!:").strip().lower()
    if command=="quit":
      active=False
      print("THANKS FOR YOUR OPERATION HERO! WE KNOW YOU WILL BE BACK HERE FOR US.")
    elif command in ["inventory","inv"]:
      if player["Inventory"]:
        print(f"YOUR INVENTORY HAS:{'->'.join(player["inventory"])}")
      else:
        print("YOU HAVE AN EMPTY INVENTORY.")
    elif command.startswith("take"):
      item_to_take=command[5:].strip()
      if item_to_take in room_data["items"]:
        room_data["items"].remove(item_to_take)
        player["inventory"].append(item_to_take) 
        print(f">THE {item_to_take} ADDED TO THE INVENTORY.")
      else:
        print(f"ITEM NOT FOUND.... THERE'S NO {item_to_take} HERE!")
    elif command in ["north", "south", "east", "west"]:
        if command in room_data["exits"]:
            destination = room_data["exits"][command]
            
            if destination.lower() == "command_bridge" and "security_keycard" not in player["inventory"]:
                print("\n[ACCESS DENIED] 🚨 RED SIRENS FLASH!")
                print("THE BLAST DOOR IS SEALED TIGHT. SECURITY KEYCARD REQUIRED.")
            else:
                player["location"] = destination
                if destination.lower()=="command_bridge":
                   print(f"security_keycard worked yeahhh you got into: {player['location']}")
                print(f"YOU MOVED {command.upper()} TO THE {player['location'].upper()}.")
        else:
            print("UNABLE TO MOVE FORWARD: PATH IS BLOCKED BY A HUGE BULKHEAD.")
            
    else:
        print("INVALID COMMAND. PLEASE ENTER A VALID DIRECTION OR 'quit'.")
