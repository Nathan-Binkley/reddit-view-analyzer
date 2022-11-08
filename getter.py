import keys
import praw


reddit = praw.Reddit(client_id=keys.client_id,client_secret=keys.client_secret,username=keys.username,password=keys.password,user_agent="testscript by /u/MinimumArmadillo2394")

subreddit = reddit.subreddit("shortsqueeze")

print("Reddit is read only:", reddit.read_only)

urls = []

for submission in subreddit.top(time_filter="month", limit=1000):
    print(submission.permalink)
    urls.append(submission.permalink)

with open("urls.txt", "w") as f:
    for url in urls:
        f.write(url + "\n")