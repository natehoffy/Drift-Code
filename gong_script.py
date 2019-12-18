import pandas as pd

file = "/Users/nhoffelmeyer/Desktop/Drift-Code/gong_data.json"

df = pd.read_json(file, orient='columns')

print(df.head(10))