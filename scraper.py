import requests
from bs4 import BeautifulSoup
from player import Player
base_url = "logs.tf/"
cur_log = 1
player_list = []
while cur_log < 100:
    cur_url = base_url + cur_log
    page = requests.get(cur_url)
    

