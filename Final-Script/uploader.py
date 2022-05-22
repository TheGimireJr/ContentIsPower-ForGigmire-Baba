import os
import os.path
import sys
import upload_video

default_description = '''Love Griffins?! So do I! Congratulations! You've stumbled upon the best channel to get short videos on the Griffins. 
Just subscribe and press the bell icon to get the notifications about which Griffin is friggin killing today!
#FamilyGuy

This is a individually managed channel with sole intention of sharing funnies of Griffins and make people smile.

P.S.: Subscribe for a cookie


family guy
peter griffin
family guy full episodes
family guy full episodes no cuts
family guy dark humor
family guy offensive jokes
family guy underrated jokes
stewie griffin
stewie on steroids,brian griffin,family guy full nocuts,family guy new episode,family guy full episode,gigmire,daily family guy,griffins family,animated shorts,adventure time shorts,rick and morty'''
default_categoryId = "23"
default_tags = 'family guy,peter griffin,family guy full episodes,family guy full episodes no cuts,family guy dark humor,family guy offensive jokes,family guy underrated jokes,stewie griffin,stewie on steroids,brian griffin,family guy full nocuts,family guy new episode,family guy full episode,gigmire,daily family guy,griffins family,animated shorts,adventure time shorts,rick and morty'

try:
    f = open("D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\constdesc.txt", encoding='utf-8')
    default_description = f.read()
    f.close()
except Exception as e:
    default_description = default_description

try:
    f = open("D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\consttags.txt", encoding='utf-8')
    default_tags = f.read()
    f.close()
except Exception as e:
    default_tags = default_tags



def checks():
    # check if client_secret.json and credentials.txt files are present
    if not os.path.isfile(".D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\client_secrets.json"):
        print(
            "[!] Client Secret file is missing. Make sure you download it from your GCP dashboard and place it in the current directory")
        sys.exit(0)

    if not os.path.isfile("D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\credentials.txt"):
        # Trigger flask server to enable use to authenticate with their account
        print("[!] credentials.txt is missing!")
        print(
            "[!] You need to initially authenticate with your Google Account so that the video can be uploaded to your channel. Don't worry, you only need to do this once.")
        print("[-] Run config.py to authenticate with your google account and create credentials.txt")

def main(title, video, privacy):
    yt_title = title
    yt_description = default_description
    yt_tags = default_tags
    yt_categoryId = default_categoryId
    yt_privacyStatus = privacy


    if yt_privacyStatus.lower() not in ["public", "private", "unlisted"]:
        print("[!] Invalid privacy status")




    print("[*] Uploading video to YouTube. This might take a while..be patient, do not close the script.")
    videoId = upload_video.upload(video, yt_title, yt_description, yt_tags, yt_categoryId, yt_privacyStatus)

    if videoId is not None:
        print("[*] Succesfully uploaded video. ")
        print("[*] https://www.youtube.com/watch?v=%s" % videoId)

    else:
        print("[!] Video upload failed.")

    return videoId