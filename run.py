from pypresence import Presence
import time
import glob
import os
from slippi import Game

client_id = '638163525029724180' #Put your client ID here
RPC = Presence(client_id) 
RPC.connect() 

while True:
    list_of_files = glob.glob('D:\Jogos\Slippi\*')
    sorted_files = sorted(list_of_files, key=os.path.getctime)
    game = Game(sorted_files[-2])
    stage = str(game.start.stage)[6:]
    playing_with = []
    for player in game.metadata.players:
        if player is None:
            char = "fox"
        elif player.netplay is None:
            char = "fox"
        else:
            if player.netplay.code == "BOGA#158":
                char = str(list(player.characters.keys())[0])[16:]
            else:
                playing_with.append(player.netplay.code)
    
    if len(playing_with) == 1:
        melee_type = "Melee Singles"
    else:
        melee_type = "Melee Doubles"


    playing_with_str = "vs."
    for code in playing_with:
        playing_with_str += " " + code

    try:
        if char == "CAPTAIN_FALCON":
            char_image = 'falcon'
            char_text = 'Captain Falcon'
        elif char == "ICE_CLIMBERS":
            char_image = 'iceclimbers'
            char_text = "Ice Climbers"
        elif char == "DONKEY_KONG":
            char_image = "donkeykong"
            char_text = 'Donkey Kong'
        elif char == "GAME_AND_WATCH":
            char_image = 'gaw'
            char_text = "Mr. Game and Watch"
        elif char == "YOUNG_LINK":
            char_image = 'younglink'
            char_text == "Young Link"
        elif char == "DR_MARIO":
            char_image = 'drmario'
            char_text == "Doctor Mario"
        else:
            char_image = char.lower()
            char_text = char.capitalize()
        
    except:
        continue


    if stage == "POKEMON_STADIUM":
        stage_text = "Pokemon Stadium"
        stage_image = "ps"
    elif stage == "FOUNTAIN_OF_DREAMS":
        stage_text = "Fountain of Dreams"
        stage_image = "fod"
    elif stage == "YOSHIS_STORY":
        stage_text = "Yoshi's Story"
        stage_image = "yoshis"
    elif stage == "DREAM_LAND_N64":
        stage_text = "Dreamland"
        stage_image = "dl"
    elif stage == "BATTLEFIELD":
        stage_text = "Battlefield"
        stage_image = "bf"
    elif stage == "FINAL_DESTINATION":
        stage_text = "Final Destination"
        stage_image = "fd"


    print(RPC.update(state=playing_with_str, details=melee_type, large_image=stage_image, small_image=char_image, large_text=stage_text, small_text=char_text, buttons=[{'label':'On testing',"url":'https://github.com/miguelrcborges/'}]))
    time.sleep(10)




