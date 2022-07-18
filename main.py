import instaloader
import numpy as np
import time

loader = instaloader.Instaloader()

# Login or load session
username = ""
password = ""
loader.login(username, password)  # (login)

# Obtain profile metadata
profile = instaloader.Profile.from_username(loader.context, username)

# Print list of followees
follower_list = []
following_list = []
count = 0
for follower in profile.get_followers():
    count += 1
    if count < 800:
        follower_list.append(follower.username)
    else:
        time.sleep(10)
        count = 0
    
count = 0
for following in profile.get_followees():
    count += 1
    if count < 800:
        following_list.append(following.username)
    else:
        time.sleep(10)
        count = 0

not_following_back = np.setdiff1d(following_list, follower_list)
print(len(follower_list))
print(len(following_list))
print(not_following_back)
