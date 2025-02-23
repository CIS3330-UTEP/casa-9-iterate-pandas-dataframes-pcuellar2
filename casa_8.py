import pandas as pd
#read and open file
df = pd.read_csv('big-mac-full-index.csv')

#Method 4: Using iterrows() method
# Iterating over rows based on website example
for index, row in df.iterrows():
        if row['iso_a3'] == 'USA' and row['date'] >= '7/1/2021':
            print(f"Date: {row['date']}") 
            print(f"Local Price: {row['local_price']}")

#Method 6: Using apply() methods
def localpricechange(row):
    last_calculated_price = 5.58
    if row['iso_a3'] == 'USA':
        return f"{row['name']} Change of Price: ${last_calculated_price - row['local_price']}"

result = df.apply(localpricechange, axis=1)
for res in result:
    print(res)