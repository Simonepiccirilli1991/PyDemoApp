import pandas as pd

response = pd.read_html("https://it.wikipedia.org/wiki/Guerra_di_Crimea")


print(response)
# concatenate all DataFrames into a single DataFrame
df = pd.concat(response)

print(df)
# check if the text exists in the DataFrame
if df.values.__contains__('Omar Pascià'):
    print("ce sta")
else:
    print('non ce sta')
