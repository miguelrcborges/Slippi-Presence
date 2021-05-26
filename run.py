import time
import configparser
import glob
import os
from slippi import Game
from pypresence import Presence

config = configparser.ConfigParser()
config.read('config.ini')
path = config['Variables']['path']
code = config['Variables']['code']

support_dict = {"CAPTAIN_FALCON":['falcon','Captain Falcon'], "ICE_CLIMBERS": ['iceclimbers', "Ice Climbers"], "DONKEY_KONG": ["donkeykong", "Donkey Kong"], "GAME_AND_WATCH": ['gaw', "Mr. Game and Watch"], "YOUNG_LINK": ['younglink', "Young Link"], "DR_MARIO": ['drmario',"Doctor Mario"]}
stages_dict = {"POKEMON_STADIUM": ['ps','Pokemon Stadium'], "FOUNTAIN_OF_DREAMS": ['fod', 'Fountain of Dreams'], "YOSHIS_STORY": ["yoshis", "Yoshi's Story"], "DREAM_LAND_N64": ['dl', 'Dreamland'], "BATTLEFIELD": ['bf',"Battlefield"], "FINAL_DESTINATION": ['fd','Final Destination']}

client_id = '638163525029724180' 
RPC = Presence(client_id) 
RPC.connect() 

while True:
    list_of_files = glob.glob(path + ".\*")
    sorted_files = sorted(list_of_files, key=os.path.getctime)
    game = Game(sorted_files[-2])
    stage = str(game.start.stage)[6:]
    playing_with = []
    for player in game.metadata.players:
        if player is None:
            pass
        else:
            if str(player.netplay.code) == code:
                char = str(list(player.characters.keys())[0])[16:]
            else:
                playing_with.append(player.netplay.code)
    
    if len(playing_with) == 1:
        melee_type = "Melee Singles"
    else:
        melee_type = "Melee Doubles"


    playing_with_str = "vs."
    for person in playing_with:
        playing_with_str += " " + person

    try:
        if char in support_dict.keys():
            char_image, char_text = support_dict[char]
        else:
            char_image = char.lower()
            char_text = char.capitalize()
    
    except:
        continue

    try:
        stage_image, stage_text = stages_dict[stage]

    except:
        pass


    print(RPC.update(state=playing_with_str, details=melee_type, large_image=stage_image, small_image=char_image, large_text=stage_text, small_text=char_text, buttons=[{'label':'On testing',"url":'https://github.com/miguelrcborges/'}]))
    time.sleep(10)




