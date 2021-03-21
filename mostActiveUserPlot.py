##
# This Python Script plots all users who ever talked in a channel onto a bar chart.
# Do not use this script if the channel you are analyzing has had a large number of people type in it
# If a channel has had more than 100ish people type in it you are going to want to modify this script and cut off the lower end of the data
##

import json
from matplotlib import pyplot as plt

general = open('FileNameHere.json', 'r')

generalPhrased = json.load(general)

data = dict()

for i in generalPhrased['messages']: # Iterates through each message in the JSON file and stores them as i
    if i['author']['name'] in data:
        # If the author of this particular message is in the dictionary then increment their message count by one
        data[i['author']['name']] = data[i['author']['name']] + 1
    else:
        # If the author of the message is not in the dictionary then add them to the list
        data[i['author']['name']] = 1


for key in list({key: value for key, value in sorted(data.items(), key=lambda item: item[1])}):
    print(key, ":", data[key])

sortedData = {key: value for key, value in sorted(data.items(), key=lambda item: item[1])}

# This controls the size of the plot and the numbers represent width and height respectively
# Edit them as you see fit, don't be afraid to mess around with them.
plt.figure(figsize=(30, 15))

plt.xticks(rotation=90)
plt.xlabel('Names')
plt.ylabel('Number of messages in [Channel Name Here]')
plt.title('Who talks the most in [Channel Name Here]?')

plt.tick_params(labeltop=False, labelright=True)

## This can sometimes crop out text so use at your discression
# plt.tight_layout()

plt.bar(*zip(*sortedData.items()))

plt.show()
