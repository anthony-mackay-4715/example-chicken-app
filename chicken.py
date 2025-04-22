import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import re 

#Set the page configuration
st.set_page_config(page_title="Chicken Recipes", layout="wide")

#Create a title and subheader
st.title('Chicken Recipes Example App')
st.write("This is an example web app built using chicken recipes from [All Recipes](https://www.allrecipes.com/)." )

#Read in and display the data
data = pd.read_csv('chicken_recipes.csv')

# Add sliders for filtering by prep time and total time
st.sidebar.header("Filter Recipes")

# Get min and max values for the sliders
min_prep_time = int(data['Prep Time (mins)'].min())
max_prep_time = int(data['Prep Time (mins)'].max())
min_total_time = int(data['Total Time (mins)'].min())
max_total_time = int(data['Total Time (mins)'].max())
min_calories = int(data['Calories'].min())
max_calories = int(data['Calories'].max())
min_rating = float(data['Review Rating'].min())
max_rating = float(data['Review Rating'].max())
min_reviews = int(data['Review Count'].min())
max_reviews = int(data['Review Count'].max())

# Create the sliders
prep_time_range = st.sidebar.slider(
    "Prep Time (mins)",
    min_value=min_prep_time,
    max_value=max_prep_time,
    value=(min_prep_time, max_prep_time)
)

total_time_range = st.sidebar.slider(
    "Total Time (mins)",
    min_value=min_total_time,
    max_value=max_total_time,
    value=(min_total_time, max_total_time)
)

calorie_range = st.sidebar.slider(
    "Calories",
    min_value=min_calories,
    max_value=max_calories,
    value=(min_calories, max_calories)
)

rating_range = st.sidebar.slider(
    "Review Rating",
    min_value=min_rating,
    max_value=max_rating,
    value=(min_rating, max_rating)  
)

review_count_range = st.sidebar.slider(
    "Review Count",
    min_value=min_reviews,
    max_value=max_reviews,
    value=(min_reviews, max_reviews)    
)

# Filter the data based on slider values
filtered_data = data[
    (data['Prep Time (mins)'] >= prep_time_range[0]) & 
    (data['Prep Time (mins)'] <= prep_time_range[1]) &
    (data['Total Time (mins)'] >= total_time_range[0]) & 
    (data['Total Time (mins)'] <= total_time_range[1]) &
    (data['Calories'] >= calorie_range[0]) &
    (data['Calories'] <= calorie_range[1]) &
    (data['Review Rating'] >= rating_range[0]) &
    (data['Review Rating'] <= rating_range[1]) &
    (data['Review Count'] >= review_count_range[0]) &
    (data['Review Count'] <= review_count_range[1])
]

# Add in a subheader for the filtered data
st.header('List of Recipes')
# Display the filtered data
st.dataframe(filtered_data, hide_index=True)

# Show number of recipes after filtering
st.write(f"Showing {len(filtered_data)} recipes out of {len(data)} total recipes")

# Add in a subheader for the histogram
st.header('Distribution of Calories')
# Create a histogram of the calories
fig, ax = plt.subplots()
ax.hist(filtered_data['Calories'], bins=20)
ax.set_xlabel('Calories')
ax.set_ylabel('Number of Recipes')
st.pyplot(fig)