import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit.components.v1 as components


st.title('Finding insights.')
df = pd.read_csv("student_habits_performance.csv")

with st.container():
    
    
    st.subheader("Choose a factor to see how it affects exam scores.")
    
    user_input = st.selectbox('',
                                   ['study_hours_per_day',
                                    'social_media_hours',
                                    'attendance_percentage',
                                    'sleep_hours',
                                    'mental_health_rating',
                                    'extracurricular_participation'
                                    ] , 
                                   key='factor')
    bin_labels=[]
    if user_input == "study_hours_per_day":
        bins = np.linspace(0, 8.3, 6)
        bin_labels = [f"{round(bins[i],1)} - {round(bins[i+1],1)} " for i in range(len(bins)-1)]

    elif  user_input == "social_media_hours": 
        if "netflix_hours" in df.columns:
            df['social_media_hours']+=df['netflix_hours']
        bins = np.linspace(0,8,5)
        bin_labels = [f"{round(bins[i],1)} - {round(bins[i+1],1)} " for i in range(len(bins)-1)]
    
    elif user_input=='attendance_percentage':
        bins= np.arange(0,110,10)
        bin_labels = [f'{bins[i]}-{bins[i+1]}' for i in range(len(bins)-1)]

    elif user_input == 'mental_health_rating':
        bins = np.arange(1,12,1)
        bin_labels = [str(i) for i in range(1,11)]

    elif user_input=='sleep_hours':
        bins = np.arange(3,11,1)
        bin_labels = [str(i) for i in range(3,10)]

    elif user_input == 'extracurricular_participation':
        res = df.groupby(user_input)['exam_score'].mean().reset_index()
        res[user_input] = res[user_input].astype(str)
        st.bar_chart(res.set_index(user_input))
        st.stop()
    df['binned'] = pd.cut(df[user_input],bins=bins, labels=bin_labels, include_lowest=True, right=False)

    scorebin = df.groupby('binned')['exam_score'].mean().reset_index()
    scorebin = scorebin.dropna()

    st.line_chart(scorebin.set_index('binned'))

    st.write("From the about graphs, it is observed that:")
    st.write("-> Study hours are inversely proportional to exam scores.")
    st.write("-> Sleep hours are directly proportional to exam scores.")
    st.write("-> Social media/screen time and mental health rating are also inversely proportional to exam scores.")
    st.write("Note: There WILL always be outliers.")



with st.container():
    
    st.subheader("Correlation matrix (numeric values)")
    numeric_df = df.select_dtypes(include=['number']) 
    corr_matrix = numeric_df.corr()
    # st.write(corr_matrix)

    fig,ax = plt.subplots(figsize=(10,8))
    sns.heatmap(corr_matrix,annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=  ax)

    st.pyplot(fig)


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