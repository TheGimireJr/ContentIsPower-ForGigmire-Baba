from pymongo import MongoClient
import requests
from termcolor import colored
from Link_finder import link_finder
from ytDownloader import ytDownloader
from Editor import editor
import uploader
import datetime
from mail import send_mail

try:
    client = MongoClient("mongodb+srv://Giggity:xa4RiXPA5MiBSrir@linkinventory.ds1ks.mongodb.net/Stage1Auto?retryWrites=true&w=majority")
    db = client['Stage1Auto']
    scraped = db['ScrapedLinks']
    daily = db['Daily']
    mails = db['mailDB']
    print(colored('Connection to database successful...', 'green'))
except:
    print(colored('Couldn\'t connect to the database...', 'red'))

# Creating message for each step
body = 'The connection to DataBase was successful...\n'

real_link = False

while real_link == False:
    downloader_output = ''
    link = link_finder(scraped, daily)
    downloader_output = ytDownloader(link)
    cdn = downloader_output['link']
    vidTitle = downloader_output['title']

    if vidTitle.find('Family') or vidTitle.find('family') != 1:
        real_link = True
    else:
        real_link = False

# Creating message for each step
body += 'The link found successfully...\n'

# Downloading
r = requests.get(cdn, allow_redirects=True)
open('D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\RawVid.mp4', 'wb').write(r.content)

# Creating message for each step
body += 'The video downloaded successfully...\n'


# Editing
editor('D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\RawVid.mp4')

# Creating message for each step
body += 'The video edited successfully...\n'


# Creating Title
raw_title = vidTitle
final_title = f'{raw_title} | #Shorts #FamilyGuy #PeterGriffin #Quagmire'

# Creating message for each step
body += 'The title was created successfully...\n'

# Final-Upload
vID = uploader.main(final_title, 'D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\\final.mp4', 'unlisted')

# Creating message for each step
body += 'The video was uploaded successfully...\n\n'
body += f'Video title: {final_title} \n Privacy: Public \n Link: www.youtube.com/shorts/{vID}'


now = datetime.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

subject = f'{raw_title} uploaded on {date} at {time}'


send_mail(mails, subject, body)








