import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

def get_user_events(username):
    response = requests.get('https://api.github.com/users/{}/events'.format(username))
    return response.json()




if __name__ == "__main__":
    username = sys.argv[1]

    events = get_user_events(username)


    print(" - User: {} has a total of {} events".format(username,
                                                       len(events)
                                                        ))

    print(" - The first is a \"{}\" type event, created on {}".format(events[0]['type'],
                                                                      events[0]['created_at']
                                                                      ))