import json
import pandas as pd
league_roster=[ 
    {
    "name":"red",
    "region":"johto",
    "ace":{
        "pokemon":"charizard",
        "type":["fire"],
        "attack":{
            "name":"fire_blast",
            "stat":85
        },
        "bond":95
        },
},
{
    "name":"misty",
    "region":"kanto",
    "ace":{
        "pokemon":"starmie",
        "type":["water","psychic"],
        "attack":{
        "name":"watergun",
        "stat":70,
        },
        "bond":65
    },
}
]
for trainers in league_roster:
 if trainers["name"]=="misty":
  pronoun="she"
 else:
  pronoun="he"
 print(f"=====WE Have HERE TRAINER {trainers['name'].upper()} AND THE BEST POKEMON {pronoun.upper()} HAS IS {trainers['ace']['pokemon'].upper()}")
with open("league_roster.json","r")as file:
  vault_data=json.load(file)
print(f"\n[VAULT CHECK] MISTY'S NEW BOND SCORE WITH HER POKEMON IS : {vault_data[1]['ace']['bond']}%")
    