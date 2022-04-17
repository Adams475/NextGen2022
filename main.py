# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def read_data():
    data = pd.read_csv("C:\\Users\\13174\\Desktop\\Hackathon\\Summary_Basket_2020.csv")
    return data
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    data = read_data()
    cols = data.columns
    print(data.head())
    online = data.loc[data['Online'] == 1].to_numpy()
    person = data.loc[data['Online'] == 0]
    i=0
    for e in online[:, 2]:
        online[i, 2] = str('20') + str(e)
        i += 1
    on = pd.DataFrame(online, columns=cols)
    x = [datetime.strptime(d, '%Y-%m-%d').date() for d in on['date']]
    x1 = sorted(set(x))
    y = []
    j = 0
    for date in sorted(set(online[:, 2])):
        print(date)
        a = np.where(online[:, 2] == date)
        y.append(sum(online[a[0], 4]))
        print(y[j])
        j += 1
    DF = pd.DataFrame()
    DF['x'] = x1
    DF['y'] = y
    plt.scatter(x1, y)
    plt.gcf().autofmt_xdate()
    plt.show()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
