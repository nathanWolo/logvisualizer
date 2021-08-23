import requests
from bs4 import BeautifulSoup
from player import Player
import re
base_url = "http://logs.tf/"
cur_log = 1
player_dict = {}
player_list = []
while cur_log < 1000:
    cur_url = base_url + str(cur_log)
    page = requests.get(cur_url)
    soup = BeautifulSoup(page.content, "html.parser")
    players = soup.find_all("tr", id = re.compile("player_\d{17}"))
    steam_idre = re.search("player_\d{17}", str(players))
    if steam_idre:
        steam_id = steam_idre.group(0)
        steam_id = steam_id[7:]
        if steam_id in player_dict.keys():
            player_dict[steam_id] += 1
        else:
            player_dict[steam_id] = 1
            player_list.append(steam_id)
    cur_log += 1
    print(cur_log)
sorted_list = sorted(player_list, key = lambda k: player_dict[k], reverse=True)
for p in sorted_list:
    print("SteamID:" + p + "  Games Played:" + str(player_dict[p]))

