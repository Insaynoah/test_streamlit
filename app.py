import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title("Basic Streamlit App")

# Sidebar with user input
st.sidebar.header("User Input")
user_name = st.sidebar.text_input("Enter your name:", "User")
user_number = st.sidebar.slider("Select a number:", 1, 100, 50)

# Greeting based on user input
st.write(f"Hello, {user_name}! You selected the number {user_number}.")

# Generating and displaying data
st.header("Random Data Table")
data_size = st.slider("Number of rows in the table:", 5, 100, 10)
data = pd.DataFrame(
    np.random.randn(data_size, 3),
    columns=["Column A", "Column B", "Column C"]
)
st.dataframe(data)

# Plotting a chart
st.header("Chart Example")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Series A", "Series B", "Series C"]
)
st.line_chart(chart_data)

# Displaying a Matplotlib figure
st.header("Matplotlib Plot Example")
fig, ax = plt.subplots()
ax.plot(chart_data.index, chart_data["Series A"], label="Series A")
ax.plot(chart_data.index, chart_data["Series B"], label="Series B")
ax.plot(chart_data.index, chart_data["Series C"], label="Series C")
ax.set_title("Matplotlib Line Plot")
ax.legend()
st.pyplot(fig)

# Footer
st.write("This is a simple Streamlit app example. Enjoy!")
