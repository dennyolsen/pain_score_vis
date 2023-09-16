import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta

dates = ['2018-12-20', '2018-12-21', '2018-12-22', '2018-12-23', '2018-12-24', '2018-12-25', '2018-12-26', '2018-12-27', '2018-12-28']
#dates = ['2018-12-20']

data = pd.read_csv('data.csv')
data['datetime'] = pd.to_datetime(data['datetime'])
data.index = data.datetime

# for date in data.datetime:
#     print(pd.to_datetime(date))

for date in dates:
    plt.plot(data.score[date:date], linestyle='dotted', color='red')
    plt.ylim(0, 10)
    plt.xlim(pd.to_datetime(date), pd.to_datetime(date) + timedelta(days=1))
    plt.title('Pain Scores, ' + date)
    plt.show()
