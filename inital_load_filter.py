import pandas as pd

data = pd.read_csv("pp-complete-top100.csv")
data.columns = [
    "id",
    "price",
    "sale_date",
    "postcode",
    "unknown",
    "unknown",
    "unknown",
    "PAON",
    "SAON",
    "street",
    "locality",
    "town/city",
    "district",
    "county",
    "unknown",
    "unknown",
]

# Preview the first 5 lines of the loaded data
print(data.head())
#print( "hey")
print("hey")
