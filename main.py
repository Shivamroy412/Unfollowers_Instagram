import instaloader
import numpy as np
import time
import sys
import config

loader = instaloader.Instaloader()

# Fetch user credentials from config.py file
# Enter your Instagram user_id and password as Strings in the config file
# If you have two-factor authetication activated on your account, you would have to disable it

try: 
    username = config.USERNAME
    password = config.PASSWORD
    if not username or password:
        raise ValueError("Enter username and password as Strings in config file and save it.")
except ValueError as e:
    print(e)
    sys.exit(1)

# Login to the account    
loader.login(username, password)  

# Obtain profile metadata
profile = instaloader.Profile.from_username(loader.context, username)

# The below code extracts information from Instagram servers, however for some users the
# Instagram server would throw an error after certain number of continous extractions to pass
# through this error, a lag of 10 seconds has been incorporated after every 800 extractions
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


print(f"The user {username} has {len(follower_list)} followers.")
print(f"The user is following {len(following_list)} accounts")
print(f"Below is the list of accounts being followed by {username} who are not following back:")
for user in not_following_back: print(user)
