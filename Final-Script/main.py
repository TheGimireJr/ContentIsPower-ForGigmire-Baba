from pymongo import MongoClient
import requests
from termcolor import colored
from Link_finder import link_finder
from ytDownloader import ytDownloader
from Editor import editor
import uploader

try:
    client = MongoClient("mongodb+srv://Giggity:xa4RiXPA5MiBSrir@linkinventory.ds1ks.mongodb.net/Stage1Auto?retryWrites=true&w=majority")
    db = client['Stage1Auto']
    scraped = db['Scraped-dummy']
    daily = db['Daily-dummy']
    print(colored('Connection to database successful...', 'green'))
except:
    print(colored('Couldn\'t connect to the database...', 'red'))

real_link = False

while real_link == False:
    link = link_finder(scraped, daily)
    downloader_output = ytDownloader(link)
    cdn = downloader_output['link']
    vidTitle = downloader_output['title']

    if vidTitle.find('Family') or vidTitle.find('family') != 1:
        real_link = True
    else:
        real_link = False

# Downloading
r = requests.get(cdn, allow_redirects=True)
open('D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\RawVid.mp4', 'wb').write(r.content)

# Editing
editor('D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\RawVid.mp4')

# Creating Title
raw_title = vidTitle
final_title = f'{raw_title} | #Shorts #FamilyGuy #PeterGriffin #Quagmire'

# Final-Upload
vID = uploader.main(final_title, 'D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\\final.mp4', 'unlisted')









