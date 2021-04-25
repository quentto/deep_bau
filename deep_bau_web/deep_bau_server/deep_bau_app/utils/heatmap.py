import pandas as pd
import numpy as np
import datetime as dt
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from io import StringIO

df = pd.read_csv('/home/tquentel/projects/SDaCathon/deep_bau/data/features/df_deep_bau.csv', index_col=0)


def viz_process(df, topic, project_id, date):

    df = df[df["BaustelleID"] == project_id]
    df = df.tail(date)
        
    df = df.loc[:, (df != 0).any(axis=0)]
    
    df.set_index(df["Datum"], inplace=True)
    df = df.filter(regex=topic)
    df.columns = df.columns.str.replace(f'{topic}_', '')
    
    col_set = df.columns.to_list()
    order = []
    for i in range(date):
        test = df.iloc[i,:]
        activities = [col_set[a] for a, x in enumerate(test) if x > 0]
        
        for activity in activities:
            if activity not in order:
                order.append(activity)
        
    df = df[order]
    
    df = df.transpose()
    df.replace(0, np.nan, inplace=True)
    
    fig, ax = plt.subplots(1, 1)
    #sns.set_style(style='white')
    sns.set(rc={'figure.figsize':(10,5)})
    
    cmap=sns.cm.rocket_r
    sns.heatmap(df, cmap=cmap, square=True, annot=True, cbar=0)
    
    for i in range(df.shape[1]+1):
        ax.axhline(i, color='white', lw=2)
        
    #xticks = ax.get_xticks()
    fig.autofmt_xdate()
    fig.set
    
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    
    plt.close()
    
    return data #, df

#data = viz_process(df, "Tätigkeit", 101227, 100)