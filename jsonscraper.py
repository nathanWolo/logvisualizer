import re
from bs4 import BeautifulSoup
import requests
from player import Player
import json
def steamid_to_64bit(steamid):
    steam64id = 76561197960265728 # I honestly don't know where
                                    # this came from, but it works...
    id_split = steamid.split(":")
    steam64id += int(id_split[2]) * 2 # again, not sure why multiplying by 2...
    if id_split[1] == "1":
        steam64id += 1
    return steam64id
base_url = "http://logs.tf/json/"
cur_log = 900
player_dict = {}
unique_players_in_log = []
cur_url = base_url + str(cur_log)
page = requests.get(cur_url)
steam_idre = re.findall("STEAM_[0-1]:[0-1]:\d{6,9}", str(page.text))
player_dict = dict.fromkeys(steam_idre, 1)
#print(player_dict)
player_set = set(steam_idre)
logs_base_page = "https://logs.tf/profile/"
while cur_log < 1000:
    print("Currently scraping log #" + str(cur_log))
    cur_log += 1
    cur_url = base_url + str(cur_log)
    page = requests.get(cur_url)
    steam_idre = re.findall("STEAM_[0-1]:[0-1]:\d{6,9}", str(page.text))
    steam_id_set = set(steam_idre)
    for p in steam_id_set:
        if p in player_set:
            player_dict[p] += 1
        else:
            player_dict[p] = 1
            player_set.add(p)
sorted_list = sorted(player_set, key = lambda k: player_dict[k], reverse=True)
for p in sorted_list[:10]:
    steam64 = steamid_to_64bit(p)
    profile = logs_base_page + str(steam64)
    log_page = requests.get(profile)
    log_soup = BeautifulSoup(log_page.content, "html.parser")
    name = log_soup.find("h3")

    print("Player Name: " + str(ascii(name.text)) + "  Games Played:" + str(player_dict[p]))