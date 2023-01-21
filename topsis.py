import pandas as pd
import math as m

def topsis(data, impacts, weights):
#   data = pd.read_csv(path)
    rows = len(data.axes[0])
    cols = len(data.axes[1])

    df = pd.DataFrame.copy(data, deep=True)
#   weights = [int(e) for e in weight.split(',')]
#   impacts = impact.split(',')

    for i in range(1,cols):
        df.iloc[:,i] *= weights[i-1]

    best = []
    worst = []
    for i in range(1,cols):
        if impacts[i-1]=='+':
            best.append(max(df.iloc[:,i]))
            worst.append(min(df.iloc[:,i]))
        if impacts[i-1]=='-':
            best.append(min(df.iloc[:,i]))
            worst.append(max(df.iloc[:,i]))

    d_best=[]
    d_worst=[]
    for i in range(rows):
        d_best.append(m.dist(df.iloc[i,1:],best))
        d_worst.append(m.dist(df.iloc[i,1:],worst))
    
    topsis = []
    for i in range(rows):
        topsis.append((d_worst[i])/(d_best[i]+d_worst[i]))

    data["Topsis Score"] = topsis
    data['Rank'] = (data['Topsis Score'].rank(method='max', ascending=False))
    data = data.astype({"Rank": int})
    # data.iloc[:,-1].to_frame().style.highlight_max(color = 'lightgreen', axis = 0)