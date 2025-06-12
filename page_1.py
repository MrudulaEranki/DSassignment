import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import streamlit.components.v1 as components


st.title("Student Habits vs Academic Performance.")
st.write(
    "Dashboard to identify habit patterns and external factors of students to show how they affect the exam score."
)


with st.container():
    
    
    col1,col2 = st.columns([5,1],gap="small",vertical_alignment="top",border=False)

    with col1:
        
        df = pd.read_csv("student_habits_performance.csv")
        age_counts = df['age'].value_counts().sort_index()
        age_range = np.arange(17,25)
        chart_data  = pd.DataFrame({
            "age":age_range,
            "count":[age_counts.get(age,0) for age in age_range ]
        })

        # bar chart not clickable
        st.bar_chart(chart_data,x="age",y="count")
        # age_selector = alt.selection_point(fields=["age"], bind="legend", name="Select")
        # bar_chart = alt.Chart(chart_data).mark_bar().encode(
        #     x=alt.X("age:O", title="Age"),
        #     y=alt.Y("count:Q", title="Number of Students"),
        #     color=alt.condition(age_selector, alt.value("steelblue"), alt.value("lightgray")),
        #     tooltip=["age", "count"]
        # ).add_params(age_selector)

        # st.altair_chart(bar_chart, use_container_width=True)
    selected_age = st.selectbox("Select Age", age_range)
    show_all = st.checkbox("Show all ages (revert to full dataset)", value=False)

    if show_all:
        filtered_df = df
    else:
        filtered_df = df
        filtered_df = df[df['age']==selected_age]
        
    male_count =(filtered_df['gender'] == 'Male').sum()
    female_count =(filtered_df['gender'] == 'Female').sum()
    other_count = len(filtered_df) - male_count - female_count
        
    col2.metric("Male",male_count)
    col2.metric("Female",female_count)
    col2.metric("Other",other_count)
    

with st.container():
    c1 ,c2= st.columns([1,1])

    df = pd.read_csv("student_habits_performance.csv")
    
    age_range = np.arange(17,25)
    avg_scores_by_age  = df.groupby('age')['exam_score'].mean()
    min_scores = df.groupby('age')['exam_score'].min()
    max_scores = df.groupby('age')['exam_score'].max()

    chart_data2 = pd.DataFrame({
        'age':age_range,
        'min_scores': [min_scores.get(age,0) for age in age_range],
        'avg_scores': [avg_scores_by_age.get(age,0) for age in age_range],
        'max_scores': [max_scores.get(age,0) for age in age_range]
    })
    
    # c1 = st.line_chart(chart_data2.set_index('age'),[['min_scores',"max_Scores"]])
    c1 = st.line_chart(chart_data2.set_index("age")[["min_scores",'avg_scores', "max_scores"]])

    # c2 = st.line_chart(chart_data2, x = 'age',y = 'average scores')
    value = df['exam_score'].mean()
    c2.metric('total average score of 1000 students',value=value)

components.html(
    """
    <div style="position: fixed; bottom: 0; width: 100%; text-align: center; padding: 10px 0; background-color: transparent;">
        <p style="font-size: 14px; color: gray;">
            Based on this dataset 
            <a href="https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance" 
               target="_blank" style="color: #1f77b4; text-decoration: none;">
               (Kaggle)
            </a>
        </p>
    </div>
    """,
    height=50,
)