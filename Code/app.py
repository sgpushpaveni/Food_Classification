import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(r'D:\GUVI-Projects\food_calssification\Food_Classification\Data\synthetic_food_dataset_imbalanced.csv')
    return df

df = load_data()

st.title("Smart Dietary Application: Nutritional Food Recommendation")

st.markdown("""
This application helps you select foods that match your nutritional preferences.  
Set your desired ranges for calories, protein, fat, carbs, sugar, fiber, sodium, etc., and get instant recommendations!
""")

# Sidebar: Set desired nutritional ranges
st.sidebar.header("Set Your Nutritional Preferences")
calories = st.sidebar.slider("Calories", float(df['Calories'].min()), float(df['Calories'].max()), (float(df['Calories'].min()), float(df['Calories'].max())))
protein = st.sidebar.slider("Protein (g)", float(df['Protein'].min()), float(df['Protein'].max()), (float(df['Protein'].min()), float(df['Protein'].max())))
fat = st.sidebar.slider("Fat (g)", float(df['Fat'].min()), float(df['Fat'].max()), (float(df['Fat'].min()), float(df['Fat'].max())))
carbs = st.sidebar.slider("Carbs (g)", float(df['Carbs'].min()), float(df['Carbs'].max()), (float(df['Carbs'].min()), float(df['Carbs'].max())))
sugar = st.sidebar.slider("Sugar (g)", float(df['Sugar'].min()), float(df['Sugar'].max()), (float(df['Sugar'].min()), float(df['Sugar'].max())))
fiber = st.sidebar.slider("Fiber (g)", float(df['Fiber'].min()), float(df['Fiber'].max()), (float(df['Fiber'].min()), float(df['Fiber'].max())))
sodium = st.sidebar.slider("Sodium (mg)", float(df['Sodium'].min()), float(df['Sodium'].max()), (float(df['Sodium'].min()), float(df['Sodium'].max())))
cholesterol = st.sidebar.slider("Cholesterol (mg)", float(df['Cholesterol'].min()), float(df['Cholesterol'].max()), (float(df['Cholesterol'].min()), float(df['Cholesterol'].max())))
glycemic_index = st.sidebar.slider("Glycemic Index", float(df['Glycemic_Index'].min()), float(df['Glycemic_Index'].max()), (float(df['Glycemic_Index'].min()), float(df['Glycemic_Index'].max())))
is_vegan = st.sidebar.selectbox("Vegan?", ["Any", "TRUE", "FALSE"])
is_gluten_free = st.sidebar.selectbox("Gluten-Free?", ["Any", "TRUE", "FALSE"])

# Filter data based on user input
filtered = df[
    (df['Calories'] >= calories[0]) & (df['Calories'] <= calories[1]) &
    (df['Protein'] >= protein[0]) & (df['Protein'] <= protein[1]) &
    (df['Fat'] >= fat[0]) & (df['Fat'] <= fat[1]) &
    (df['Carbs'] >= carbs[0]) & (df['Carbs'] <= carbs[1]) &
    (df['Sugar'] >= sugar[0]) & (df['Sugar'] <= sugar[1]) &
    (df['Fiber'] >= fiber[0]) & (df['Fiber'] <= fiber[1]) &
    (df['Sodium'] >= sodium[0]) & (df['Sodium'] <= sodium[1]) &
    (df['Cholesterol'] >= cholesterol[0]) & (df['Cholesterol'] <= cholesterol[1]) &
    (df['Glycemic_Index'] >= glycemic_index[0]) & (df['Glycemic_Index'] <= glycemic_index[1])
]

if is_vegan != "Any":
    filtered = filtered[filtered['Is_Vegan'] == is_vegan]
if is_gluten_free != "Any":
    filtered = filtered[filtered['Is_Gluten_Free'] == is_gluten_free]

st.subheader("Recommended Foods Matching Your Preferences")
st.write(f"Found {len(filtered)} foods matching criteria.")
st.dataframe(filtered[['Food_Name','Meal_Type','Preparation_Method','Calories','Protein','Fat','Carbs','Sugar','Fiber','Sodium','Is_Vegan','Is_Gluten_Free']])

# Visualize selected food
st.subheader("Macro Distribution for Selected Food")
selected_food = st.selectbox("Select a food to visualize", filtered['Food_Name'].unique() if len(filtered) else df['Food_Name'].unique())
food_row = df[df['Food_Name'] == selected_food].iloc[0]

labels = ['Protein', 'Fat', 'Carbs', 'Sugar', 'Fiber']
sizes = [food_row[l] for l in labels]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.set_title(f"Macro Breakdown: {selected_food}")

st.pyplot(fig)

st.markdown("""
---
**Business case:**  
This app can be used by nutritionists, fitness coaches, and consumers for smart dietary planning, menu selection, and healthy eating recommendations based on personal goals or medical needs.
""")