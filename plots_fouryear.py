import plotly.express as px
from data_loader import load_data
import streamlit as st

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

q1toq5_columns = ['name', 'state','kq5_cond_parq1','par_q1','tier_name','par_median', 'count']  

# Function to create a scatter plot
def plot_fouryear_q1toq5_all():

    # Load the dataset
    df = load_data("four")

    # filter count > 500
    df = df[df['count'] > 500]

    fig = px.scatter(
        df,
        x='kq5_cond_parq1',
        y='par_median',
        size='count',
        color='tier_name',
        hover_name='name',
        color_discrete_map=tier_colors,
        title="Bottom Quintile to Second Quintile",
        labels={'kq5_cond_parq1': 'Mobility Rate: Q1 to Q5', 'par_median': 'Parent Median Income'},
    )
    # Update x-axis to format as percentage
    fig.update_layout(
        xaxis_tickformat='.0%'
    )
    return fig


def plot_fouryear_q1toq5_top():
    
    # Load the dataset
    df = load_data("four")


    df = df[q1toq5_columns]

    # filter par_q1 > 0.10
    df = df[df['par_q1'] > 0.10]

    # filter count > 500
    df = df[df['count'] > 500]

    # Sort the data by kq2_cond_parq1
    df = df.sort_values(by='kq5_cond_parq1', ascending=False).head(50)

    
    fig = px.scatter(
        df,
        x='kq5_cond_parq1',
        y='par_median',
        size='count',
        color='tier_name',
        hover_name='name',
        color_discrete_map=tier_colors,
        title="Top Performers: Bottom Quintile to Top Quintile",
        labels={'kq5_cond_parq1': 'Mobility Rate: Q1 to Q5', 'par_median': 'Median Parent Income'},
    )
     # Update x-axis to format as percentage
    fig.update_layout(
        xaxis_tickformat='.0%'
    )
    return fig




def plot_other(df):
    # Placeholder function for other sub-options
    fig = px.scatter(
        df,
        x='kq2_cond_parq1',
        y='par_median',
        size='count',
        color='tier',
        title="Other: Parent Median Income vs. Mobility from Bottom Quintile to Second Quintile",
        labels={'kq2_cond_parq1': 'Mobility Rate (Q1 to Q2)', 'par_median': 'Median Parent Income'},
    )
    return fig