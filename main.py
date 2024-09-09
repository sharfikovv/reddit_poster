import praw
import random
import schedule
import time
from datetime import datetime
import prawcore
from img_upload import upload_image_to_imgur

with open('creds.txt', 'r') as file:
    for line in file:
        client_id, client_secret, user_agent, username, password = line.strip().split(' - ')

try:
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent,
                         username=username,
                         password=password)
except NameError:
    client_id = input('Input your Reddit client ID: ')
    client_secret = input('Input your Reddit client secret: ')
    user_agent = input('Input your Reddit user agent: ')
    username = input('Input your Reddit username: ')
    password = input('Input your Reddit password: ')

    with open('creds.txt', 'w') as file:
        file.write(client_id + " - " + client_secret + " - " + user_agent + " - " + username + " - " + password)

    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent,
                         username=username,
                         password=password)


def schedule_posts():
    with open('schedule.txt', 'r') as file:
        for line in file:
            subreddit_name, day, post_time, photo_file, titlefile, flair = line.strip().split(' - ')
            hrs, mns = post_time.split(':')
            hrs = str(hrs)
            mns = int(mns) + random.randint(-15, 15)
            if mns < 10:
                mns += 30
            if mns >= 60:
                mns -= 20
            schedule.every().day.at(hrs + ":" + str(mns)).do(post_to_subreddit, subreddit_name, photo_file, titlefile,
                                                             flair, day)
            print(subreddit_name, "scheduled at", hrs, "hours", mns, "mins")


def post_to_subreddit(subreddit_name, photo_file, titlefile, flair_text, day):
    current_day = datetime.now().strftime('%A').lower()
    if current_day == day.lower():
        try:
            with open(titlefile, 'r') as file:
                titles = file.readlines()
                title = random.choice(titles).strip()

            with open(photo_file, 'r') as file:
                photos = file.readlines()
                photo_upload = random.choice(photos).strip()
                photo_url = upload_image_to_imgur(photo_upload)

            subreddit = reddit.subreddit(subreddit_name)

            flairs = list(subreddit.flair.link_templates)
            flair_id = next((flair['id'] for flair in flairs if flair['text'].lower() == flair_text.lower()), None)
            print("Publishing to ", subreddit_name, photo_url)
            subreddit.submit(title, url=photo_url, flair_id=flair_id)
            print("Published successfully!")
        except prawcore.exceptions.Forbidden:
            with open(titlefile, 'r') as file:
                titles = file.readlines()
                title = random.choice(titles).strip()

            with open(photo_file, 'r') as file:
                photos = file.readlines()
                photo_upload = random.choice(photos).strip()
                photo_url = upload_image_to_imgur(photo_upload)

            subreddit = reddit.subreddit(subreddit_name)
            print("Publishing to ", subreddit_name, photo_url)
            subreddit.submit(title, url=photo_url)
            print("Published successfully!")
        except prawcore.exceptions.NotFound:
            print("SUBREDDIT DOESNT EXIST (OR BANNED)", subreddit_name)

    else:
        print("")


schedule_posts()

while True:
    schedule.run_pending()
    time.sleep(1)
