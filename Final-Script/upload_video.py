import os

import google_auth_oauthlib.flow
import google.oauth2.credentials

import googleapiclient.discovery
import googleapiclient.errors

from googleapiclient.http import MediaFileUpload
import ast

scopes = ["https://www.googleapis.com/auth/youtube.upload"]
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


def upload(filename, title, description, tags, categoryId, privacyStatus):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = 'D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\client_secrets.json'

    try:
        body = dict(snippet=dict(title=title, description=description, tags=tags,
                                 categoryId=categoryId
                                 ),
                    status=dict(privacyStatus=privacyStatus))

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)

        f = open('D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\credentials.txt', 'r')
        creds = ast.literal_eval(f.read())
        f.close()
        credentials = google.oauth2.credentials.Credentials(**creds)
        # credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        request = youtube.videos().insert(
            notifySubscribers=True,
            part=",".join(body.keys()),
            body=body,

            # TODO: For this request to work, you must replace "YOUR_FILE"
            #       with a pointer to the actual file you are uploading.
            media_body=MediaFileUpload(filename)
        )
        response = request.execute()
        print(response)
        # videoId = ast.literal_eval(response)['id']
        videoId = response['id']
        return videoId

    except Exception as e:
        print("[!!] ERROR - %s" % e)
        return None


def manual_upload():
    filename = input("[+] File path: ")
    yt_title = input("[+] Video Title: ")
    yt_description = input("[+] Video Description (leave empty for default description)")
    yt_tags = input("[+] Video Tags (seperated by comas): ")
    yt_categoryId = input("[+] Category ID (Leave empty for Gaming): ")
    yt_privacyStatus = input("[+] Privacy Status (public/private/unlisted): ")

    if yt_title == "":
        print("[!] Title can't be empty")

    if yt_privacyStatus.lower() not in ["public", "private", "unlisted"]:
        print("[!] Invalid privacy status")

    if yt_description == "":
        yt_description = default_description

    if yt_categoryId == "":
        yt_categoryId = default_categoryId


    upload(filename, yt_title, yt_description, yt_tags, yt_categoryId, yt_privacyStatus)


if __name__ == "__main__":
    manual_upload()