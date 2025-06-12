import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components



page_1 = st.Page("page_1.py",title="General overview", icon=":material/home:")
page_2 = st.Page("page_2.py",title="Detailed insights", icon=":material/expand_circle_down:")

# pg = st.navigation([st.Page(page_1),st.Page(page_2)])






pg = st.navigation(
    {
        "Menu":[page_1,page_2],
        # "Reports":[page_2]
    }
)
pg.run()





# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# st.text_input("Your name", key="name")
# st.session_state.name

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

# chartdata = pd.DataFrame(
#     np.random.randn(20,3),
#     columns=['a','b','c']
# )

# chartdata

# st.line_chart(chartdata)

# mapdata = pd.DataFrame(
#     np.random.randn(1000,2) / [50,50] + [17.4065, 78.4772],
#      columns=['lat', 'lon'])


# st.map(mapdata)

# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

