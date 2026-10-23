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
    if player["health"]<=0:
       print("\n[critical Faliure]black devil is no more concious")
       print("GAME OVER!...HEROES BODY WILL FLOAT INSIDE THE NEBULA ZERO UNTIL ETURNITY!!!")
       active=False
       break
    print(f"\n========================================")
    print(f"OPERATIVE:{player['name'].upper()}| HP:{player['health']}/400")
    print(f"CURRENT SECTOR : {current_room.upper()}")
    room_data=ship_map[current_room]
    print(f"============================")
    print(room_data["desc"])
    if room_data["items"]:
     print(f"\nITEMS FOUND INTHEE ROOM ARE:{'->'.join(room_data["items"])}")
    else:
      print("NO ITEMS ARE TO BE SEEN IT THE ROOM!SHIT.")
    available_exits=list(room_data["exits"].keys())
    print(f"EXITS AVAILABLE: {', '.join(available_exits)}")
    command= input("\nAction !!move,Take <item>,Inventory,quit,heal!!:").strip().lower()
    if command=="quit":
      active=False
      print("THANKS FOR YOUR OPERATION HERO! WE KNOW YOU WILL BE BACK HERE FOR US.")
    elif command in ["reboot","escape","reboot_core"]:
       if player["location"].lower()=="command_bridge":
          print("\n"+"=" * 50)
          print(" [REACTOR ONLINE]SYSTEM RESTORATION COMPLETE!")
          print("sub-light engines roar to life. Atmosphere stabilizes.")
          print("OUR HERO BLACK DEVIL PILOTS NEBULA ZERO OUT OF THE DEAD SECTOR.")
          print("MISSION ACCOMPLISHED YOU WON THE GAME !!.....!!THANKYOU HERO FOR SAVING NEBULA ZERO !!......")
          active = False
          break
       else:
          print("ACCESS DENIED. THE SHIP CORE CAN ONLY BE REBOOTED FROM THE COMMAND BRIDGE TERMINAL!!")
    elif command in ["use medkit","heal"]:
       if "medkit" in player["inventory"]:
          heal_amount = 170
          player["health"]=min(400,player["health"]+heal_amount)
          player["inventory"].remove("medkit")
          print(f"\n PLAYER USED A MEDKIT ={heal_amount}HP IS RESTORED.!! ")
          print(f"CURRENT HEALTH : {player['health']/400}")
       else:
          print("---->YOU DO NOT HAVE HAVE A MEDKIT IN YOUR CURRENT INVENTORY!<----")
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
                print("\n[ACCESS DENIED] !! RED SIRENS FLASH !!")
                print("THE BLAST DOOR IS SEALED TIGHT. SECURITY KEYCARD REQUIRED.")
            else:
                player["location"] = destination
            if destination.lower()=="command_bridge":
                   print(f"security_keycard worked yeahhh you got into: {player['location']}")
            if destination.lower()=="armory":
                      damage=30
                      player["health"] -=damage
                      print(f"\n WARNING!!!!! YOUR HEALTH IS DAMAGED DUE TO THE AUTOMATED SECURITY TURRENTS FIRE ON YOU!! (-{damage}HP)")
                      print(f"YOU MOVED {command.upper()} TO THE {player['location'].upper()}.")
        else:
            print("UNABLE TO MOVE FORWARD: PATH IS BLOCKED BY A HUGE BULKHEAD.")
    else:
        print("INVALID COMMAND. PLEASE ENTER A VALID DIRECTION OR 'quit'.")
