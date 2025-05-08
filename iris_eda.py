import pandas as pd

# Load the dataset
df = pd.read_csv(
    'iris.csv',
    names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
)

# Display info and first 5 rows
print(df.info())       # Shows summary info
print(df.head())       # Shows top 5 rows
df.describe()