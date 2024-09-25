import streamlit as st
import plotly.express as px
from data_loader import load_data
import pandas as pd

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
def plot_enroll_top1pc():
    # Load the dataset
    df = load_data("four")


    # sort by top1pc
    df = df.sort_values(by='par_top1pc', ascending=False).head(25)

    fig = px.scatter(
        df,
        x='par_top1pc',
        y='par_median',
        size='count',
        color='tier_name',
        hover_name='name',
        color_discrete_map=tier_colors,
        title="Highest Enrollment of Top 1% Parental Income",
        labels={'par_top1pc': 'Percentage from Top 1%', 'par_median': 'Parent Median Income'},
    )
    # Update x-axis to format as percentage
    fig.update_layout(
        xaxis_tickformat='.0%'
    )
    return fig


# Function to create a scatter plot
def plot_enroll_toppt1pc():
    # Load the dataset
    df = load_data("four")

    # sort by toppt1pc
    df = df.sort_values(by='par_toppt1pc', ascending=False).head(25)
    

    fig = px.scatter(
        df,
        x='par_toppt1pc',
        y='par_median',
        size='count',
        color='tier_name',
        hover_name='name',
        color_discrete_map=tier_colors,
        title="Highest Enrollment of Top .1% Parent Median Income",
        labels={'par_top1pc': 'Percentage from Top .1%', 'par_median': 'Parent Median Income'},
    )
    # Update x-axis to format as percentage
    fig.update_layout(
        xaxis_tickformat='.0%'
    )
    return fig


# Function to create a scatter plot
def plot_inc_distribution():
    # Load the dataset
    df = load_data("four")

    # Filter for par_median 
    df = df[df['par_median'] > 150000]

    # Filter for fraction from toppt1pc > 0.02
    df = df[df['par_top1pc'] >= .15]

    # Calculate the average of the parental income distribution columns
    columns_to_average = ['par_q1', 'par_q2', 'par_q3', 'par_q4', 'par_q5']
    average_values = df[columns_to_average].mean()

    # Create a DataFrame for plotting
    average_df = pd.DataFrame({
        'Parental Income Quintile': ['Bottom 20%', 'Second 20%', 'Middle 20%', 'Fourth 20%', 'Top 20%'],
        'Average': average_values
    })

    # Create a bar plot for the average of the selected columns
    fig = px.bar(
        average_df, 
        x='Parental Income Quintile', 
        y='Average',
        title='Average Distribution of Parental Income Quintiles',
        labels={'Average': 'Average Proportion', 'Parental Income Quintile': 'Income Quintile'},
        text=average_values.apply(lambda x: f'{x:.2%}')
    )

    # Update layout to decrease the size of the plot
    fig.update_layout(
        width=600,  # Set the width of the plot
        height=400  # Set the height of the plot
    )

    # Show the plot
    return fig