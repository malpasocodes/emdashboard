import plotly.express as px
import streamlit as st
from data_loader import load_data


q1toq2_columns = ['name', 'state','kq2_cond_parq1', 'kq5_cond_parq1' ,'tier','par_median', 'count']
q1toq5_columns = ['name', 'state','kq5_cond_parq1', 'kq2_cond_parq1' ,'tier','par_median', 'count']
    

# Function to create a scatter plot
def list_twoyear_q1toq2_all():

    # Load the dataset
    df = load_data("two")

    # filter columns
    df = df[q1toq2_columns]

    # Sort the data by kq2_cond_parq1
    df = df.sort_values(by='kq2_cond_parq1', ascending=False)

    # Convert kq2_cond_parq1 to percentage with no decimals
    df['kq2_cond_parq1'] = (df['kq2_cond_parq1'] * 100).round(0).astype(int).astype(str) + '%'

    # Convert kq2_cond_parq1 to percentage with no decimals
    df['kq5_cond_parq1'] = (df['kq5_cond_parq1'] * 100).round(0).astype(int).astype(str) + '%'

    df.columns = ['Name', 'State', 'Q1toQ2 Mobility Rate', 'Q1toQ5 Mobility Rate', 'Tier', 'Parent Income Median', 'Cohort Count']

    st.write("Two Year Colleges: Student Mobility from Bottom Quintile to Second Quintile")

    return df


# Function to create a scatter plot
def list_twoyear_q1toq2_top50():

    # Load the dataset
    df = load_data("two")

    # filter columns
    df = df[q1toq2_columns]

    # cohort count > 500
    df = df[df['count'] > 1000]

    # Sort the data by kq2_cond_parq1
    df = df.sort_values(by='kq2_cond_parq1', ascending=False).head(50)

    # Convert kq5_cond_parq1 to percentage with no decimals
    df['kq2_cond_parq1'] = (df['kq2_cond_parq1'] * 100).round(0).astype(int).astype(str) + '%'

     # Convert kq2_cond_parq1 to percentage with no decimals
    df['kq5_cond_parq1'] = (df['kq5_cond_parq1'] * 100).round(0).astype(int).astype(str) + '%'

    df.columns = ['Name', 'State', 'Q1toQ2 Mobility Rate', 'Q1toQ5 Mobility Rate', 'Tier', 'Parent Income Median', 'Cohort Count']

    st.write("Two Year Colleges: Top 50 Performers - Student Mobility from Bottom Quintile to Second Quintile")
    st.write("Cohort Count > 1000")


    return df



# Function to create a scatter plot
def list_twoyear_q1toq5_all():

    # Load the dataset
    df = load_data("two")

    # filter columns
    df = df[q1toq5_columns]

    # Sort the data by kq2_cond_parq1
    df = df.sort_values(by='kq5_cond_parq1', ascending=False).head(50)

    # Convert kq5_cond_parq1 to percentage with no decimals
    df['kq2_cond_parq1'] = (df['kq2_cond_parq1'] * 100).round(0).astype(int).astype(str) + '%'

    # Convert kq5_cond_parq1 to percentage with no decimals
    df['kq5_cond_parq1'] = (df['kq5_cond_parq1'] * 100).round(0).astype(int).astype(str) + '%'

    df.columns = ['Name', 'State', 'Q1toQ5 Mobility Rate', 'Q1toQ2 Mobility Rate', 'Tier', 'Parent Income Median', 'Cohort Count']


    return df


# Function to create a scatter plot
def list_twoyear_q1toq5_top50():

    # Load the dataset
    df = load_data("two")

    # filter columns
    df = df[q1toq5_columns]

    # cohort count > 500
    df = df[df['count'] >= 1000]

    # Sort the data by kq2_cond_parq1
    df = df.sort_values(by='kq5_cond_parq1', ascending=False).head(50)

    # Convert kq5_cond_parq1 to percentage with no decimals
    df['kq5_cond_parq1'] = (df['kq5_cond_parq1'] * 100).round(0).astype(int).astype(str) + '%'

    #Convert kq5_cond_parq1 to percentage with no decimals
    df['kq2_cond_parq1'] = (df['kq2_cond_parq1'] * 100).round(0).astype(int).astype(str) + '%'

    df.columns = ['Name', 'State', 'Q1toQ5 Mobility Rate', 'Q1toQ2 Mobility Rate', 'Tier', 'Parent Income Median', 'Cohort Count']
 

    st.write("Two Year Colleges: Top 50 Performers - Student Mobility from Bottom Quintile to Top Quintile")
    st.write("Cohort Count >= 1000")


    return df


