import streamlit as st
import plotly.graph_objs as go
import pandas as pd
from plots_fouryear import plot_fouryear_q1toq5_all, plot_fouryear_q1toq5_top
from plots_wealth_elite import plot_enroll_top1pc, plot_enroll_toppt1pc, plot_inc_distribution
from plots_twoyear import plot_twoyear_q1toq2_all, plot_twoyear_q1toq2_top, plot_twoyear_q1toq5_all, plot_twoyear_q1toq5_top
from lists_twoyear import list_twoyear_q1toq2_all, list_twoyear_q1toq2_top50, list_twoyear_q1toq5_all, list_twoyear_q1toq5_top50
from lists_fouryear import list_fouryear_q1toq5_all, list_fouryear_q1toq5_top50, list_fouryear_composite_top50

# Sidebar setup
st.sidebar.title("Navigation")

# Level 1: Top-level choices
level_1_choices = ["Home", "Two-Year Colleges", "Four-Year Colleges", "Colleges Serving Wealthiest"]
level_1_choice = st.sidebar.selectbox("Select a Section", level_1_choices)

# Logic for Home (no second level)
if level_1_choice == "Home":
    st.title("Student Economic Mobility App")  
    st.write("Welcome to the student economic mobility analysis dashboard. This dashboard allows you to explore data on economic mobility at different types of colleges.")

    st.write(
        "The data used in this dashboard is sourced mostly from the "
        "[Opportunity Insights Project](https://opportunityinsights.org). "
        "Please note that any errors or interpretations of the data should not "
        "be attributed to the Opportunity Insights project."
    )
    
    st.write("The dashboard is work in progress and we welcome your feedback and suggestions.")

    st.header("Definitions")
    st.write("1. **Economic Mobility**: We can define economic mobility as the ability of a person, familiy, or group to improve their economic status over time."
             " In this dashboard, we focus on the economic mobility of students who attend different colleges.")
    st.write("2. **Fading American Dream**: The term *'Fading American Dream'* refers to the idea that the economic mobility of students in the United States has been declining over time."
             " According to the Opportunity Insights Project, *'The defining feature of the American Dream is upward mobility – "
             "the aspiration that all children have a chance at economic success, no matter their background. "
             "However, our research shows that children's chances of earning more than their parents have been declining.'"
             "90% of children born in 1940 grew up to earn more than their parents. Today, only half of all children earn more than their parents did.'*")
    
    st.write("3. **Restoring the American Dream**: The term *'Restoring the American Dream'* refers to the idea that the economic mobility of students in the United States can be improved over time."
             "With this dashboard, we aim to provide insights into the economic mobility of students who attend different colleges.")
    
    st.write("4. **Income Quintiles and Generational Mobility**: Our basic unit of analysis will be economic quintiles. Our analysis will focus on generational mobility. If a student's parents belong to a certain income quintile (e.g. Q1),"
            "what is the probability they can move up to a higher income quintile (e.g. Q2, Q3, Q4, Q5) when they attend a particular college.")
    
    # Center the image using st.columns
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("images/quintiles.png", width=300, use_column_width=False)
     
# Logic for when another section is selected
else:
    # Level 2: Sub-choices based on the Level 1 choice
    if level_1_choice == "Two-Year Colleges":
        level_2_choices = ["Two-Year: All Q1toQ2 (Viz)", "Two-Year: All Q1toQ2 (List)", "Two-Year: Top25 Q1toQ2 (Viz)", "Two-Year: Top25 Q1toQ2 (List)", "Two-Year: All Q1toQ5 (Viz)", "Two-Year: All Q1toQ5 (List)", "Two-Year: Top25 Q1toQ5 (Viz)", "Two-Year: Top25 Q1toQ5 (List)"]
    elif level_1_choice == "Four-Year Colleges":
        level_2_choices = ["Four-Year: All Q1toQ5 (Viz)", "Four-Year: All Q1toQ5 (List)", "Four-Year: Top25 Q1toQ5 (Viz)", "Four-Year: Top25 Q1toQ5 (List)", "Four-Year: Composite Top25 (List)"]
      
    elif level_1_choice == "Colleges Serving Wealthiest":
        level_2_choices = ["Enroll Most 1%", "Enroll Most .1%", "Income Distribution"]
       

    # Let the user pick a Level 2 option
    level_2_choice = st.sidebar.selectbox("Select a Sub-section", level_2_choices)

    # Display selected sub-section and generate the plot
    # st.title(f"{level_1_choice} - {level_2_choice}")
    


    # Define a dictionary mapping level_2_choice to plotting functions
    plot_functions = {
        "Two-Year: All Q1toQ2 (Viz)": plot_twoyear_q1toq2_all,
        "Two-Year: Top25 Q1toQ2 (Viz)": plot_twoyear_q1toq2_top,
        "Two-Year: All Q1toQ5 (Viz)": plot_twoyear_q1toq5_all,  
        "Two-Year: Top25 Q1toQ5 (Viz)": plot_twoyear_q1toq5_top,   
        "Four-Year: All Q1toQ5 (Viz)": plot_fouryear_q1toq5_all, 
        "Four-Year: Top25 Q1toQ5 (Viz)": plot_fouryear_q1toq5_top,
        "Enroll Most 1%": plot_enroll_top1pc,
        "Enroll Most .1%": plot_enroll_toppt1pc,
        "Income Distribution": plot_inc_distribution

    }

    list_functions = {
    "Two-Year: All Q1toQ2 (List)": list_twoyear_q1toq2_all,
    "Two-Year: Top25 Q1toQ2 (List)": list_twoyear_q1toq2_top50,
    "Two-Year: All Q1toQ5 (List)": list_twoyear_q1toq5_all,
    "Two-Year: Top25 Q1toQ5 (List)": list_twoyear_q1toq5_top50,
    "Four-Year: All Q1toQ5 (List)": list_fouryear_q1toq5_all,
    "Four-Year: Top25 Q1toQ5 (List)": list_fouryear_q1toq5_top50,
    "Four-Year: Composite Top25 (List)": list_fouryear_composite_top50
}

    # Determine the function type and call the appropriate function
    if level_2_choice in plot_functions:
        plot_function = plot_functions[level_2_choice]
        scatter_plot = plot_function()
        if scatter_plot is not None and isinstance(scatter_plot, go.Figure):
            st.plotly_chart(scatter_plot)
        else:
            st.error("The plot function did not return a valid Plotly figure.")
    elif level_2_choice in list_functions:
        list_function = list_functions[level_2_choice]
        df = list_function()
        if df is not None and isinstance(df, pd.DataFrame):
            df = df.reset_index(drop=True)
            df.index += 1
            st.write(df)
        else:
            st.error("The list function did not return a valid DataFrame.")
    else:
        st.error("Invalid selection. Please choose a valid sub-section.")

        

