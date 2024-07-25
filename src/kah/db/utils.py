import pandas as pd

def read_data(path="~/data/parquet"):
    df = pd.read_parquet(path)
    return df

def top(count, dt):
    df = read_data()
    fdf = df[df['dt'] == dt]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(count)
    ddf = sdf.drop(columns=['dt'])
    
    # r = ddf.to_string(index=False)
    return ddf

def count(query):
    df = read_data()
    fdf = df[df['cmd'] == query]
    cnt = fdf['cnt'].sum()
    return cnt
