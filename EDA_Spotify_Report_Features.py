import pandas as pd 
from pandas_profiling import ProfileReport

df =pd.read_csv('Features.csv')
profile = ProfileReport(df, title="Spotify Report")
profile.to_file("EDA_Spotify_Report_Features.html")