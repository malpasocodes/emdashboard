import pandas as pd

# Function to load data from a CSV file
def load_data(institution_type):
    df = pd.read_csv('data/mrc_table2.csv')
    # Drop rows where 'count' is missing
    df = df.dropna(subset=['count'])

     # Convert 'count' column to integer
    df['count'] = df['count'].astype(int)   

    
    # Filter based on institution type
    if institution_type == "two":
        # df = df[(df['tier'] == 9) | (df['tier'] == 11)]
        df = df[df['iclevel']==2]
    elif institution_type == "four":
        df = df[df['iclevel']==1]
         # df = df[(df['tier'] == 1) | (df['tier'] == 2) | (df['tier'] == 3) | (df['tier'] == 4)]

    
    return df

