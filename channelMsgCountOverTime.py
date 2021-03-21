from datetime import datetime
from matplotlib import pyplot as plt
import json

general = open('fileNameHere.json', 'r')

generalPhrased = json.load(general)

previousDate = ''
msgsPerDay = 0

dates = []
msgCount = []

for time in generalPhrased['messages']:
    phrasedDate = datetime.strptime(time['timestamp'][:10], "%Y-%m-%d")
    if phrasedDate != previousDate:
        previousDate = phrasedDate
        dates.append(previousDate)
        msgCount.append(msgsPerDay)
        print(previousDate, ' : ', msgsPerDay)
        msgsPerDay = 0
    else:
        msgsPerDay = msgsPerDay + 1

# So, the code above has all dates and msg counts misaligned by one shift to the right.
# This code just deletes the leading zero and appends the correct value.
del msgCount[0]
msgCount.append(msgsPerDay)

print(dates)
print(msgCount)

# This controls the size of the plot and the numbers represent width and height respectively
# Edit them as you see fit, don't be afraid to mess around with them.
plt.figure(figsize=(50, 15))

plt.plot_date(dates, msgCount, linestyle='solid')

plt.xlabel('Time')
plt.ylabel('Number of messages in the [Channel Name Here] per day')
plt.title('Number of messages sent in [Channel Name Here] graphed over time')

# plt.tight_layout()
plt.tick_params(labeltop=False, labelright=True)
plt.gcf().autofmt_xdate

plt.show()
