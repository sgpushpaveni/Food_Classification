# NutriClass: Food Classification & Smart Dietary Recommendation

## Overview
NutriClass is a machine learning project that classifies foods based on nutritional data and powers a smart dietary recommendation app. Users can filter foods by nutritional needs, receive ML-driven suggestions.

## Features
- Data exploration and visualization
- Automated data cleaning and preprocessing
- Feature engineering (PCA, SelectKBest, encoding)
- Multiple ML classifiers benchmarked (Logistic Regression, Decision Tree, Random Forest, KNN, SVM, XGBoost, Gradient Boosting)
- Performance metrics and visualizations
- Streamlit app for personalized food recommendation and meal planning
- ML-based personalized recommendations (KNN-based)


## Dataset
- **File:** `synthetic_food_dataset_imbalanced.csv`
- **Columns:** Calories, Protein, Fat, Carbs, Sugar, Fiber, Sodium, Cholesterol, Glycemic_Index, Water_Content, Serving_Size, Meal_Type, Preparation_Method, Is_Vegan, Is_Gluten_Free, Food_Name

## Project Structure
```
├── app.py                # Streamlit app (main file)
├── NutriClass_Food_Classification.ipynb  # Analysis and ML notebook
├── README.md             # Project documentation
├── data
│  ├─ synthetic_food_dataset_imbalanced.csv            # Food nutritional data
```

## Installation

1. Clone the repository and navigate to the folder
2. Install requirements:
   ```sh
   pip install streamlit pandas scikit-learn matplotlib seaborn plotly xgboost
   ```
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## Usage

- **Notebook (`NutriClass_Food_Classification.ipynb`)**: Run all steps for data analysis, preprocessing, modeling, and evaluation.
- **App (`app.py`)**: 
  - Set nutritional goals in sidebar.
  - View food recommendations.
  - See personalized suggestions based on your selections.

## ML Approach

- Data cleaning: Impute/drop missing, cap outliers, remove duplicates, scale features
- Feature selection: PCA, SelectKBest
- Label encoding for target classes
- Models trained and compared: Logistic Regression, Decision Tree, Random Forest, KNN, SVM, XGBoost, Gradient Boosting
- Evaluation: Accuracy, Precision, Recall, F1, Confusion Matrix

## App Features

- Nutritional filter sliders (calories, protein, etc.)
- Dietary restrictions (vegan, gluten-free)
- ML-based food recommendations (KNN)
- Build and export custom meal plans
- Visual macro distribution for selected foods and meal plans

## Example Screenshots

- Food recommendations table
- Confusion matrix heatmaps
- Macro breakdown pie charts
- Model performance bar charts
