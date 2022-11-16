import pandas as pd

url="https://datacell.netlify.app/"

df=pd.read_html(url)

print(df)