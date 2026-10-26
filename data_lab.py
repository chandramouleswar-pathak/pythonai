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
df = pd.json_normalize(vault_data)
print ("\n----LEAGUE DATA DASHBOARD----")
print (df)
print (f"\n average League Bond:{df['ace.bond'].mean}%")
high_powers=df[df["ace.attack.stat"]>=80]
print("\n -----HIGH ATTACK ROASTER----")
print(high_powers[["name","ace.pokemon","ace.attack.stat"]])
elight_bond=df[df["ace.bond"]>95]
print("\n---trainers with highest bond with pokemon----")
print(elight_bond[["name","ace.bond"]])
highest_attack_power=df["ace.attack.stat"].max()
print(f"\n-----HIGHEST POWER IN LEAGUE :")
print(highest_attack_power)
df["combat_power"]=df["ace.attack.stat"]+df["ace.bond"]
print(df.sort_values(by="combat_power",ascending=False)[["name","ace.pokemon","combat_power"]])