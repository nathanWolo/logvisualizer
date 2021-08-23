import re
from bs4 import BeautifulSoup
import requests
from player import Player
import json

base_url = "http://logs.tf/json/"
cur_log = 1
player_list = []
player_dict = {}

cur_url = base_url + str(cur_log)
page = requests.get(cur_url)
logson = json.loads(page.text)
print(logson)