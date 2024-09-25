import plotly.express as px
from data_loader import load_data

tier_colors = {
    'Two-year for-profit': 'blue',
    'Selective private': 'green',
    'Nonselective four-year public': 'red',
    'Four-year for-profit': 'purple',
    'Selective public': 'orange',
    'Two-year (public and private not-for-profit)': 'green',
    'Nonselective four-year private not-for-profit': 'pink',
    'Highly selective private': 'brown',
    'Other elite schools (public and private)': 'cyan',
    'Less than two-year schools of any type': 'magenta',
    'Highly selective public': 'lime',
    'Ivy Plus': 'indigo',
    }

    

# Function to create a scatter plot
def plot_twoyear_q1toq2_all():

    # Load the dataset
    df = load_data("two")

    df = df[df['count'] >= 1000]



    fig = px.scatter(
        df,
        x='kq2_cond_parq1',
        y='par_median',
        size='count',
        color='tier_name',
        hover_name='name',
        color_discrete_map=tier_colors,
        title="Bottom Quintile to Second Quintile",
        labels={'kq2_cond_parq1': 'Mobility Rate: Q1 to Q2', 'par_median': 'Parent Median Income'},
    )

     # Update x-axis to format as percentage
    fig.update_layout(
        xaxis_tickformat='.0%'
    )
    return fig


def plot_twoyear_q1toq2_top():
    
    # Load the dataset
    df = load_data("two")

    # filter for cohort count >=500
    df = df[df['count'] >= 1000]

    # sort by mobility rate 
    df = df.sort_values(by='kq2_cond_parq1', ascending=False).head(25)

    fig = px.scatter(
        df,
        x='kq2_cond_parq1',
        y='par_median',
        size='count',
        color='tier_name',
        hover_name='name',
        color_discrete_map=tier_colors,
        title="Top50: Mobility from Bottom Quintile to Second Quintile",
        labels={'kq2_cond_parq1': 'Mobility Rate: Q1 to Q2', 'par_median': 'Median Parent Income'},
    )

     # Update x-axis to format as percentage
    fig.update_layout(
        xaxis_tickformat='.0%'
    )
    return fig

# Function to create a scatter plot
def plot_twoyear_q1toq5_all():

    # Load the dataset
    df = load_data("two")

    df = df[df['count'] >= 1000]


    fig = px.scatter(
        df,
        x='kq5_cond_parq1',
        y='par_median',
        size='count',
        color='tier_name',
        hover_name='name',
        color_discrete_map=tier_colors,
        title="Econmic Mobility: Q1 to Q5",
        labels={'kq5_cond_parq1': 'Mobility Rate: Q1 to Q5', 'par_median': 'Parent Median Income'},
    )

     # Update x-axis to format as percentage
    fig.update_layout(
        xaxis_tickformat='.0%'
    )
    return fig

def plot_twoyear_q1toq5_top():
    

    # Load the dataset
    df = load_data("two")
    
    # Sort the data by kq5_cond_parq1
    df = df.sort_values(by='kq5_cond_parq1', ascending=False).head(50)


    # filter for cohort count >=500
    df = df[df['count'] >= 1000]

    
    fig = px.scatter(
        df,
        x='kq5_cond_parq1',
        y='par_median',
        size='count',
        color='tier_name',
        hover_name='name',
        color_discrete_map=tier_colors,
        title="Top Performers: Mobility from Bottom Quintile to Top Quintile",
        labels={'kq5_cond_parq1': 'Mobility Rate: Q1 to Q5', 'par_median': 'Median Parent Income'},
    )

     # Update x-axis to format as percentage
    fig.update_layout(
        xaxis_tickformat='.0%'
    )
    return fig


