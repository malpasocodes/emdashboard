import plotly.express as px
from data_loader import load_data

q1toq5_columns = ['name', 'state','kq5_cond_parq1','par_q1','tier_name','par_median', 'count']


# Function to create a scatter plot
def list_fouryear_q1toq5_all():

    # Load the dataset
    df = load_data("four")

    # filter columns
    df = df[q1toq5_columns]

    # Sort the data by kq2_cond_parq1
    df = df.sort_values(by='kq5_cond_parq1', ascending=False)

    # Convert kq5_cond_parq1 to percentage with no decimals
    df['kq5_cond_parq1'] = (df['kq5_cond_parq1'] * 100).round(0).astype(int).astype(str) + '%'

    # Convert par_q1 to percentage with no decimals
    df['par_q1'] = (df['par_q1'] * 100).round(0).astype(int).astype(str) + '%'


    return df


# Function to create a lit of top 50 performers
def list_fouryear_q1toq5_top50():

    # Load the dataset
    df = load_data("four")

    # filter columns
    df = df[q1toq5_columns]

    # filter par_q1 > 0.10
    df = df[df['par_q1'] > 0.10]

    # filter count > 500
    df = df[df['count'] > 500]

    # Sort the data by kq2_cond_parq1
    df = df.sort_values(by='kq5_cond_parq1', ascending=False).head(50)

    # Convert kq5_cond_parq1 to percentage with no decimals
    df['kq5_cond_parq1'] = (df['kq5_cond_parq1'] * 100).round(0).astype(int).astype(str) + '%'

    # Convert par_q1 to percentage with no decimals
    df['par_q1'] = (df['par_q1'] * 100).round(0).astype(int).astype(str) + '%'


    return df



# Function to create a list of top 50 performers based on composite metric

def list_fouryear_composite_top50():

    # Load the dataset
    df = load_data("four")


    # filter par_q1 > 0.10
    df = df[df['par_q1'] > 0.10]

    # filter count > 500
    df = df[df['count'] > 500]


    # Define the updated weights for each mobility transition
    weights = {
        'kq2_cond_parq1': 3,  # Q1 to Q2 - higher weight
        'kq3_cond_parq1': 1.5,  # Q1 to Q3 - lower weight
        'kq4_cond_parq1': 1.5,  # Q1 to Q4 - lower weight
        'kq5_cond_parq1': 3    # Q1 to Q5 - higher weight
    }

    # Maximum possible score is now 3 (since the highest weight is 3)
    max_score = 3

    # Calculate the mobility score using the updated weighted sum of probabilities
    df['mobility_score'] = (
        (weights['kq2_cond_parq1'] * df['kq2_cond_parq1']) +
        (weights['kq3_cond_parq1'] * df['kq3_cond_parq1']) +
        (weights['kq4_cond_parq1'] * df['kq4_cond_parq1']) +
        (weights['kq5_cond_parq1'] * df['kq5_cond_parq1'])
    )

    # Normalize the mobility score by dividing by the maximum possible score
    df['normalized_mobility_score'] = df['mobility_score'] / max_score

    # Sort the data by normalized mobility score
    df = df.sort_values(by='normalized_mobility_score', ascending=False).head(50)

    columns = ['name', 'state', 'normalized_mobility_score', 'kq5_cond_parq1', 'kq2_cond_parq1', 'count']

    df = df[columns]




    return df

