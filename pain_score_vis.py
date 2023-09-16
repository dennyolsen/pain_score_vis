import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta

dates = ['2018-12-20', '2018-12-21', '2018-12-22', '2018-12-23', '2018-12-24', '2018-12-25', '2018-12-26', '2018-12-27', '2018-12-28']
show = False

data = pd.read_csv('data.csv')
data['datetime'] = pd.to_datetime(data['datetime'])
data.index = data.datetime

# iterate over dates and save charts to disk
for date in dates:
    plt.figure(figsize=(10, 6))
    plt.plot(data.score[date:date], linestyle='dotted', color='red')
    plt.ylim(0, 10)
    plt.xlim(pd.to_datetime(date), pd.to_datetime(date) + timedelta(days=1))
    plt.title('Pain Scores, ' + date)
    if show:
        plt.show()
    plt.savefig(date + ".png")

# create an overall chart and save to disk
plt.figure(figsize=(10, 6))
plt.plot(data.score, linestyle='dotted', color='red')
plt.ylim(0, 10)
plt.title('Pain Scores, Overall')
if show:
    plt.show()
plt.savefig("Overall.png")
