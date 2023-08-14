#Imports
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(url)
soup = bs(page.text, "html.parser")
star_table  = soup.find_all("table")
temp_list = []
for tr in star_table[7].find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_names = []
distance = []
mass =[]
radius = []

for i in range(1, len(temp_list)):

    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])


df = pd.DataFrame(list(zip(star_names, distance, mass, radius)), columns = ["Star name", "Distance", "Mass", "Radius"])
df.to_csv("Dwarf Stars.csv")